from flask_graphql import Resolve, GraphQLObjectType, GraphQLField, GraphQLNonNull, GraphQLString, GraphQLInt, GraphQLList

class Query(GraphQLObjectType):
    todos = GraphQLField(
        GraphQLList(Todo),
        resolve=Resolve(tasks.get_all_todos)
    )
    todo = GraphQLField(
        Todo,
        id=GraphQLNonNull(GraphQLInt),
        resolve=Resolve(tasks.get_todo_by_id)
    )

class Mutation(GraphQLObjectType):
    createTodo = GraphQLField(
        Todo,
        title=GraphQLNonNull(GraphQLString),
        description=GraphQLString,
        due_time=GraphQLInt,
        
      
        resolve=Resolve(tasks.create_todo)
    )
    updateTodo = GraphQLField(
        Todo,
        id=GraphQLNonNull(GraphQLInt),
        title=GraphQLString,
        description=GraphQLString,
        due_time=GraphQLInt,

      
        resolve=Resolve(tasks.update_todo)
    )
    deleteTodo = GraphQLField(
        GraphQLInt,
        id=GraphQLNonNull(GraphQLInt),
        resolve=Resolve(tasks.delete_todo)
    )