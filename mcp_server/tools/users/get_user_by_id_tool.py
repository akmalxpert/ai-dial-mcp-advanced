from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class GetUserByIdTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return 'get_user_by_id'

    @property
    def description(self) -> str:
        return 'Tool for getting user by id'

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "Id of the user to be retrieved"
                }
            },
            "required": [
                "id"
            ]
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        user_id = arguments.get('id')
        try:
            return await self._user_client.get_user(user_id)
        except Exception as e:
            return f"Error while retrieving user by id: {str(e)}"
