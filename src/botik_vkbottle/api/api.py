from botik.api.api import Api
from botik_vkbottle.api.api_type import VkApiType
from botik_vkbottle.api.send_message import VkSendMessage


class VKApi(Api):
    def __init__(self, raw_api):
        self.msg = VkSendMessage(raw_api)
        self.api_type = VkApiType()
