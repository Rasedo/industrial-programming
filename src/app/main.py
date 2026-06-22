from app.logger import log


def main() -> None:
    print("App running")
    log.warning('warning message')
    log.info('info message')
    log.debug('debug message')


if __name__ == "__main__":
    main()
