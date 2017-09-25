import socket


def wake(mac: str):
    payload = [0xff] * 6 + [int(f'0x{x}', 16) for x in mac.split(':')] * 16

    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(bytes(payload), ('ff02::1', 9))


if __name__ == 'main':
    import sys
    wol(sys.argv[1])
