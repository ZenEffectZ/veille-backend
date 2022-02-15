from .serializers import PostItemSerializer, ImageItemSerializer, CommentItemSerializer
from .models import PostItem, ImageItem, CommentItem
from rest_framework.viewsets import ModelViewSet
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


# Create your views here.

# class PostItemViewSet(FlexFieldsMixin, ModelViewSet):
#     serializer_class = PostItemSerializer
#     permit_list_expands = ['category']
#     filterset_fields = ('user',)
#
#     def get_queryset(self):
#         queryset = PostItem.objects.all()
#
#         if is_expanded(self.request, 'user'):
#             queryset = queryset.prefetch_related('user')
#
#         return queryset
class PostItemViewSet(FlexFieldsMixin, APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        print(request.user.username)
        print(request.user.id)
        # postitems = PostItem.objects.filter(user=request.user.id)
        postitems = PostItem.objects.all()
        serializer = PostItemSerializer(postitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        print("ERROR", request.user.id)
        data = {
            'content': request.data.get('content'),
            'user_id': request.user.id,
            'image': request.data.get('image')
        }
        serializer = PostItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostItemDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, post_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return PostItem.objects.get(id=post_id)
        except PostItem.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, post_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(post_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PostItemSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, post_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = PostItem.objects.filter(id=post_id, user_id=request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with post_id does not exists or not yours"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'user_id': request.user.id
        }
        serializer = PostItemSerializer(instance=todo_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, post_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        # todo_instance = self.get_object(post_id, request.user.id)
        todo_instance = PostItem.objects.filter(id=post_id, user_id=request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists or you are not the owner"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class PostsUserApiView(FlexFieldsMixin, APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.AllowAny]

    def get(self, request, user_id, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        print(user_id)
        # postitems = PostItem.objects.filter(user=request.user.id)
        postitems = PostItem.objects.filter(user_id=user_id)
        serializer = PostItemSerializer(postitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
