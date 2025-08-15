import time
from wotclientdetection import LauncherManager, LauncherFlavour, ClientBranch

manager = LauncherManager()
launchers = manager.get_launchers()
for launcher in launchers:
    client = launcher.get_client(branch=ClientBranch.COMMON_TEST)
    if client is not None:
        print(f'{'WoT' if client.realm not in ('RU', 'RPT', ) else 'MT'} v. {client.client_version}/{client.realm} [{client.path}]')
        print(f'Executable filename: {client.exe_filename}')
        if client.launcher_flavour == LauncherFlavour.LESTA and client.exe_filename == 'Tanki.exe':
            launcher.run()
            time.sleep(5)
            client.run()
            time.sleep(15)
            r = client.terminate()
            print(r)