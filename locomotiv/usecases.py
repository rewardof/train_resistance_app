from django.db.models import QuerySet
from utils.constants import CONSTANTS


class UseCases:
    @staticmethod
    def making_vagon_groups(vagons: QuerySet):
        data = {
            "group_1": {
                "count": 0,
                "vagons_ids": [],
            },
            "group_2": {
                "count": 0,
                "vagons_ids": [],
            },
            "group_3": {
                "count": 0,
                "vagons_ids": [],
            },
            "group_4": {
                "count": 0,
                "vagons_ids": [],
            },
            "group_5": {
                "count": 0,
                "vagons_ids": [],
            },
            "group_6": {
                "count": 0,
                "vagons_ids": [],
            }
        }
        for vagon in vagons:
            if vagon.number_of_arrow == 4:
                if vagon.load_weight > 0:
                    if vagon.bullet_weight > 6:
                        if vagon.vagon_type == CONSTANTS.VAGON_TYPE.PV:
                            data['group_1']['count'] += 1
                            data['group_1']['vagons_ids'].append(vagon.id)
                        elif vagon.vagon_type == CONSTANTS.VAGON_TYPE.SYS:
                            data['group_2']['count'] += 1
                            data['group_2']['vagons_ids'].append(vagon.id)
                        elif vagon.vagon_type == CONSTANTS.VAGON_TYPE.RF:
                            data['group_6']['count'] += 1
                            data['group_6']['vagons_ids'].append(vagon.id)
                        else:
                            data['group_3']['count'] += 1
                            data['group_3']['vagons_ids'].append(vagon.id)
                    else:
                        data['group_6']['count'] += 1
                        data['group_6']['vagons_ids'].append(vagon.id)
                else:
                    data['group_4']['count'] += 1
                    data['group_4']['vagons_ids'].append(vagon.id)

            else:
                data['group_5']['count'] += 1
                data['group_5']['vagons_ids'].append(vagon.id)

        return data

    @staticmethod
    def specific_resistance_for_group_one(capacity: int, bullet_weight: float):
        """
        yuklangan, 4 o'qli, 'pv' vagonlar uchun
        solishtirma qarshilik
        """
        if bullet_weight > 0:
            w = 0.53 + (3.6 + 0.08 * capacity + 0.00275 * capacity * capacity) / bullet_weight
            return w
        return 0

    @staticmethod
    def specific_resistance_for_group_two(capacity: int, bullet_weight: float):
        """
        yuklangan, 4 o'qli, 'sys' vagonlar uchun
        solishtirma qarshilik
        """
        if bullet_weight > 0:
            w = 0.642 + (2.925 + 0.0473 * capacity + 0.00275 * capacity * capacity) / bullet_weight
            return w
        return 0

    @staticmethod
    def specific_resistance_for_group_three(capacity: int, bullet_weight: float):
        """
        yuklangan, 4 o'qli, 'kr', 'pl', 'xp', 'pr' vagonlar uchun
        solishtirma qarshilik
        """
        if bullet_weight > 0:
            w = 0.7 + (3 + 0.1 * capacity + 0.0025 * capacity * capacity) / bullet_weight
            return w
        return 0

    @staticmethod
    def specific_resistance_for_group_four(capacity: int, bullet_weight: float):
        """
        yuklangan, 4 o'qli, q > 6, 'kr', 'pl', 'xp', 'pr' vagonlar uchun
        solishtirma qarshilik
        """
        if bullet_weight > 0:
            w = 1 + 0.044 * capacity + 0.00024 * capacity * capacity
            return w
        return 0

    @staticmethod
    def specific_resistance_for_group_five(capacity: int, bullet_weight: float):
        """
        8 o'qli barcha vagonlar uchun
        """
        if bullet_weight > 0:
            w = 0.7 + (6 + 0.0377 * capacity + 0.00214 * capacity * capacity) / bullet_weight
            return w
        return 0

    @staticmethod
    def specific_resistance_for_group_six(capacity: int, bullet_weight: float):
        """
        yuklanmagan, 4 va 8 o'qli barcha vagonlar uchun yoki
        yuklangan, 4 o'qli, 'rf' vagonlar uchun
        solishtirma qarshilik
        """
        if bullet_weight > 0:
            w = 0.68 + (3 + 0.1 * capacity + 0.00255 * capacity * capacity) / bullet_weight
            return w
        return 0



