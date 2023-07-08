from django_addons.user_management.options.strategies.interface import IOptionStrategy


class EmailDataOptionStrategy(IOptionStrategy):
    def fill_options(self):
        return {
            'invitation_acceptance_link': self._get(
                'email_data.invitation_acceptance_link', 'https://example.com/link/'
            )
        }
