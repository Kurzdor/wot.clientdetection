from wotclientdetection import LauncherManager

manager = LauncherManager()
launchers = manager.get_launchers()
idx = 1
for launcher in launchers:
    clients = launcher.get_clients()
    for client in clients:
        print(f'{idx}. {'WoT' if client.realm not in ('RU', 'RPT', ) else 'MT'} v. {client.client_version} / realm: {client.realm} / branch: {client.branch} / full_client_version: {client.full_client_version} / PDC status: {'' if client.is_pdc_supported else 'not '}supported/{'' if client.is_pdc_exists else 'not '}exists [{client.path}]')
        idx += 1
