import json
import sys
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ActivityConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept connection first
        await self.accept()
        
        user = self.scope.get("user", None)

        # If not authenticated, send error message but keep connection open
        if not user or not user.is_authenticated:
            await self.send(text_data=json.dumps({
                "type": "connection",
                "message": "Connected - authentication required for real-time updates"
            }))
            self.user = None
            self.group_name = None
            return

        self.user = user
        self.group_name = f"user_{user.id}"

        print(f"✅ WebSocket connected for user {user.username}", file=sys.stderr, flush=True)

        # Join per-user group
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        # Send welcome/system message
        await self.send(text_data=json.dumps({
            "type": "connection",
            "message": f"Connected to activity log as {user.username}"
        }))

    async def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def activity_message(self, event):
        # Event sent from views.perform_create
        print(f"📡 Sending activity to {self.user.username}", file=sys.stderr, flush=True)

        await self.send(text_data=json.dumps({
            "type": "activity",
            "data": event["data"]
        }))
