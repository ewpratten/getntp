import socket

class ntp_packet(object):

    leap_indecator: bool
    version: int
    mode: int # Pick 3 for client

    stratum: int # Stratum level
    poll: int # Max interval
    precision: int # Local clock precision

    root_delay: int # Total trip delay time
    root_dirpersion: int # Max error
    ref_id: int # Clock id

    ref_tm_s: int # Reference time-stamp in secs
    ref_tm_f: int # Reference time-stamp in second fractions

    orig_tm_s: int # time-stamp secs
    orig_tm_f: int # time-stamp fractions

    rx_tm_s: int # Recived ts secs
    rx_tm_f: int

    tx_tm_s: int
    tx_tm_f: int

def requestTime(server: str):
    payload = [ 0x1b, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.connect((server, 123))

    # send msg
    sock.sendto("time", (server, 123))

    return sock.recvfrom(1024)

print(requestTime("time.cloudflare.com"))


