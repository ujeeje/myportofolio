from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import CTFWriteup
from main.permissions import IsPortfolioOwnerOrReadOnly
from main.serializers import CTFWriteupSerializer
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def ctfwriteup_list(request):
    if request.method in ("GET", "HEAD"):
        writeups = CTFWriteup.objects.prefetch_related(
            "starred_by"
        ).order_by("title", "id")

        title = request.query_params.get("title", "").strip()

        if title:
            writeups = writeups.filter(title__icontains=title)

        serializer = CTFWriteupSerializer(
            writeups, many=True, context={"request": request},
        )

        return Response(serializer.data)

    serializer = CTFWriteupSerializer(
        data=request.data,
        context={"request": request},
    )

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED,
    )

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def ctfwriteup_detail(request, writeup_id):
    writeup = get_object_or_404(
        CTFWriteup.objects.prefetch_related("starred_by"),
        pk=writeup_id,
    )

    if request.method in ("GET", "HEAD"):
        serializer = CTFWriteupSerializer(
            writeup,
            context={"request": request},
        )
        return Response(serializer.data)

    if request.method == "DELETE":
        writeup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = CTFWriteupSerializer(
        writeup,
        data=request.data,
        partial=request.method == "PATCH",
        context={"request": request},
    )

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def ctfwriteup_star(request, writeup_id):
    writeup = get_object_or_404(CTFWriteup, pk=writeup_id)

    if writeup.starred_by.filter(pk=request.user.pk).exists():
        writeup.starred_by.remove(request.user)
    else:
        writeup.starred_by.add(request.user)

    serializer = CTFWriteupSerializer(
        writeup,
        context={"request": request}
    )

    return Response(serializer.data)

