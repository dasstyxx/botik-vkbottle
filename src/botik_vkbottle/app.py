from botik.app import App
from botik.templates.page_templates import PageTemplates
from botik.input.user_input import UserInput
from botik.navigation.navigation import Navigation
from botik.page.page_factory import PageFactory
from botik_vkbottle.api.api import VKApi
from botik_vkbottle.input.message_handlers.raw_message_handlers import RawMessageHandlers
from botik_vkbottle.page.page_factory import VkPageFactory


class VkApp(App):
    def start(self):
        self.bot.run_forever()

    def __init__(self, bot, raw_api, start_callback=None):
        super().__init__(bot)
        self.initialize_with_raw_api(raw_api)
        self.message_handlers = RawMessageHandlers(bot, start_callback,
                                                   self.users, self.navigator,
                                                   self.user_input, self.events)

    def initialize(self, bot):
        pass

    def initialize_with_raw_api(self, raw_api):
        api = VKApi(raw_api)
        self.navigator = Navigation()
        self.templates = PageTemplates(self.navigator)

        self._page_fac: PageFactory = VkPageFactory(api, self.navigator, self.templates, self.events)
        self.navigator.init_page_factory(self._page_fac)

        self.user_input = UserInput(self.navigator, self.users)
