from functools import reduce

from ckanext.gdi_userportal.logic.action.fetcher.prop_fetcher import PropFetcher


class ThemeFetcher(PropFetcher):
    def _get_batched_prop_values(self, batched_datasets) -> list[str]:
        themes = [dataset["theme"] for dataset in batched_datasets]
        themes = list(set(reduce(lambda themes1, themes2: themes1 + themes2, themes)))
        return themes
