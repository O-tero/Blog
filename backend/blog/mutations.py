import graphene
import graphql_jwt
from blog import models, types

# Customize the ObtainJSONWebToken behavior to include the user info
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(types.UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

# Mutation sends data to the database
class CreateUser(graphene.Mutation):
    user = graphene.Field(types.UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = models.User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class CreateComment(graphene.ObjectType):
    comment = graphene.Field(types.CommentType)
    
    class Arguements:
        content = graphene.String(required=True)
        user_id = graphene.ID(required=True)
        post_id = graphene.ID(required=True)
        
    def mutate(self, info, content, user_id, post_id):
        comment = models.Comment(
            content=content,
            user_id=user_id,
            post_id=post_id,
        )
        comment.save()
        
        return CreateComment(comment=comment)

class UpdatePostLike(graphene.Mutation):
    post = graphene.Field(types.PostType)
    
    class Arguments:
        post_id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)
        
    def mutate(self, info, post_id, user_id):
        post = models.Post.objects.get(pk=post)
        
        if post.likes.filter(pk=user_id).exists():
            post.likes.remove(user_id)
        else:
            post.likes.add(user_id)
        
        post.save()
        
        return UpdatePostLike(post=post)

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_comment = CreateComment.Field()
