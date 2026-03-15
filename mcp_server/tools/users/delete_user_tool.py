from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class DeleteUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return 'delete_users'

    @property
    def description(self) -> str:
        return "Delete a user by id"

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Id of the user to be deleted"
                }
            },
            "required": [
                "id"
            ]
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        user_id = arguments.get('id')
        try:
            return await self._user_client.delete_user(user_id)
        except Exception as e:
            return f"Error while deleting user by id: {str(e)}"