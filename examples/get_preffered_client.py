from wotclientdetection import LauncherManager, LauncherFlavour, ClientBranch

manager = LauncherManager()
launchers = manager.get_launchers()
for launcher in launchers:
    client = launcher.get_preffered_client(branch=ClientBranch.COMMON_TEST)
    if client is not None:
        print(f'{'WoT' if client.realm not in ('RU', 'RPT', ) else 'MT'} v. {client.client_version}/{client.realm} [{client.path}]')