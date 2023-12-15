import flet as ft


def get_navigation_rail():

    destination_preview = ft.NavigationDestination(
        icon=ft.icons.REMOVE_RED_EYE_OUTLINED,
        selected_icon=ft.icons.REMOVE_RED_EYE,
        label='Preview',)

    destination_event = ft.NavigationDestination(
        icon=ft.icons.BOOKMARK_BORDER,
        selected_icon=ft.icons.BOOKMARK,
        label='Event',)

    destination_settings = ft.NavigationDestination(
        icon=ft.icons.SETTINGS_OUTLINED,
        selected_icon=ft.icons.SETTINGS,
        label='Settings',)

    navigation_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE,
                                        text='Report'),
        group_alignment=-0.9,
        on_change=lambda e: print(f'selected: {e.control.selected_index}'),
        destinations=[
            destination_preview,
            destination_event,
            destination_settings,],)
    
    return navigation_rail
