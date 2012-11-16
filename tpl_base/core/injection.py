class DevContext(object):
    def __init__(self):
        from core.service.account_service import AccountService
        self.AccountService = AccountService()

        from core.service.tpl_service import TPLService
        self.TPLService = TPLService()

        from core.service.mail_service import MailService
        self.MailService = MailService()
