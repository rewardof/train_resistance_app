from django.db.models import QuerySet
from django.db.models import Sum
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

        total_data = UseCases.calculate_other_parameters_for_groups(vagons, data)
        return total_data

    @staticmethod
    def specific_resistance_for_group_one(capacity: int, bullet_weight: float):
        """
        yuklangan, 4 o'qli, 'pv' vagonlar uchun
        solishtirma qarshilik
        """
        if bullet_weight > 0:
            w = 0.53 + (3.6 + 0.08 * capacity + 0.00275 * capacity * capacity) / bullet_weight
            return round(w, 2)
        return 0

    @staticmethod
    def specific_resistance_for_group_two(capacity: int, bullet_weight: float):
        """
        yuklangan, 4 o'qli, 'sys' vagonlar uchun
        solishtirma qarshilik
        """
        if bullet_weight > 0:
            w = 0.642 + (2.925 + 0.0473 * capacity + 0.00275 * capacity * capacity) / bullet_weight
            return round(w, 2)
        return 0

    @staticmethod
    def specific_resistance_for_group_three(capacity: int, bullet_weight: float):
        """
        yuklangan, 4 o'qli, 'kr', 'pl', 'xp', 'pr' vagonlar uchun
        solishtirma qarshilik
        """
        if bullet_weight > 0:
            w = 0.7 + (3 + 0.1 * capacity + 0.0025 * capacity * capacity) / bullet_weight
            return round(w, 2)
        return 0

    @staticmethod
    def specific_resistance_for_group_four(capacity: int, bullet_weight: float):
        """
        yuklangan, 4 o'qli, q > 6, 'kr', 'pl', 'xp', 'pr' vagonlar uchun
        solishtirma qarshilik
        """
        if bullet_weight > 0:
            w = 1 + 0.044 * capacity + 0.00024 * capacity * capacity
            return round(w, 2)
        return 0

    @staticmethod
    def specific_resistance_for_group_five(capacity: int, bullet_weight: float):
        """
        8 o'qli barcha vagonlar uchun
        """
        if bullet_weight > 0:
            w = 0.7 + (6 + 0.0377 * capacity + 0.00214 * capacity * capacity) / bullet_weight
            return round(w, 2)
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
            return round(w, 2)
        return 0

    @classmethod
    def calculate_resistance_for_all_groups(cls, capacity: int, vagons_group_data: dict):
        group_1_resistance = cls.specific_resistance_for_group_one(capacity,
                                                                   vagons_group_data['group_1']['bullet_weight'])
        group_2_resistance = cls.specific_resistance_for_group_one(capacity,
                                                                   vagons_group_data['group_2']['bullet_weight'])
        group_3_resistance = cls.specific_resistance_for_group_one(capacity,
                                                                   vagons_group_data['group_3']['bullet_weight'])
        group_4_resistance = cls.specific_resistance_for_group_one(capacity,
                                                                   vagons_group_data['group_4']['bullet_weight'])
        group_5_resistance = cls.specific_resistance_for_group_one(capacity,
                                                                   vagons_group_data['group_5']['bullet_weight'])
        group_6_resistance = cls.specific_resistance_for_group_one(capacity,
                                                                   vagons_group_data['group_6']['bullet_weight'])
        total_resistance = round(
            group_1_resistance * vagons_group_data['group_1']['percentage'] + \
            group_2_resistance * vagons_group_data['group_2']['percentage'] + \
            group_3_resistance * vagons_group_data['group_3']['percentage'] + \
            group_4_resistance * vagons_group_data['group_4']['percentage'] + \
            group_5_resistance * vagons_group_data['group_5']['percentage'] + \
            group_6_resistance * vagons_group_data['group_6']['percentage'], 2
        )
        data = {
            "capacity": capacity,
            "group_1_resistance": group_1_resistance,
            "group_2_resistance": group_2_resistance,
            "group_3_resistance": group_3_resistance,
            "group_4_resistance": group_4_resistance,
            "group_5_resistance": group_5_resistance,
            "group_6_resistance": group_6_resistance,
            'total_resistance': total_resistance
        }
        return data

    @staticmethod
    def calculate_other_parameters_for_groups(vagons: QuerySet, vagons_group_data: dict):
        totol_number_vagons = vagons.count()
        for _, vagons_data in vagons_group_data.items():
            # umumiy o'qlar soni
            total_arrows = vagons.filter(
                id__in=vagons_data['vagons_ids']).aggregate(total_weight=Sum('number_of_arrow'))['total_weight']
            vagons_data['total_arrows'] = total_arrows if total_arrows else 0

            # umumiy vagonlar soniga nisbatan ulushi
            vagons_data['percentage'] = round(vagons_data['count'] / totol_number_vagons, 3)

            # guruhdagi vagonlarni umumiy og'irligi(yuk bilan)
            total_weight = vagons.filter(
                id__in=vagons_data['vagons_ids']).aggregate(total_weight=Sum('total_weight'))['total_weight']
            vagons_data['total_weight'] = round(total_weight, 2) if total_weight else 0

            # o'qqa tushadigan og'irlik
            if vagons_data['count'] == 0:
                vagons_data['bullet_weight'] = 0
            else:
                vagons_data['bullet_weight'] = round(vagons_data['total_weight'] / vagons_data['total_arrows'], 2)

        return vagons_group_data
