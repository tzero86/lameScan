import main


class ConfigMenu:
    # General settings
    lameScan_config = {
        'debug': False,
        'max_thread_workers': 60
    }

    # General scan specific settings
    scan_config = {
        'debug': False,
        'max_thread_workers': 60,
        'range': {
            'low_port': 0,
            'high_port': 65535
        },
        'sock_conn_timeout': 0.3,
        'show_closed_ports': False,
        'run_top1k_ports': False,
        'Auto_generate_report': False
    }

    def __init__(self):
        pass
