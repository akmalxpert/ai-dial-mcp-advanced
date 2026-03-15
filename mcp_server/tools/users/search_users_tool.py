from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        return 'search_users'

    @property
    def description(self) -> str:
        return 'Search users tool'

    @property
    def input_schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the user to search"
                },
                "surname": {
                    "type": "string",
                    "description": "The surname of the user to search"
                },
                "email": {
                    "type": "string",
                    "description": "The email of the user to search"
                },
                "gender": {
                    "type": "string",
                    "description": "The gender of the user to search"
                },

            },
            "required": []
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        try:
            return await self._user_client.search_users(**arguments)
        except Exception as e:
            return f"Error while searching users: {str(e)}"
