def pytest_addoption(parser):
    parser.addoption(
        "--foreman-only",
        action="store_true",
        default=False,
        help="skip katello-related steps"
    )
    parser.addoption(
        "--katello-only",
        action="store_true",
        default=False,
        help="skip foreman steps"
    )

def pytest_generate_tests(metafunc):
    if 'foreman_only' in metafunc.fixturenames:
        if metafunc.config.getoption('foreman_only'):
            metafunc.parametrize("foreman_only", [True], ids=['no_content'])
        elif metafunc.config.getoption('katello_only'):
            metafunc.parametrize("foreman_only", [False], ids=['content'])
        else:
            metafunc.parametrize(
                "foreman_only", [True, False], ids=['no_content', 'content']
            )
