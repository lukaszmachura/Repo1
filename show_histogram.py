def show_histogram(hist, znak="="):
    """drukowanie histogramu w konsoli"""
    txt_hist = ""
    keys = sorted(hist.keys())
    for key in keys:
        val = hist[key]
        bar = znak * val
        _th = "{:2d}|{}\n".format(key, bar)
        txt_hist += _th
    return txt_hist