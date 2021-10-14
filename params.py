import altair as alt


def get_scale(domain_min, domain_max):
    return alt.Scale(domain=(domain_min, domain_max), zero=False, nice=False)


def get_axis_params():
    return dict(title=None,
                ticks=False,
                tickCount=10,
                domain=False,
                gridOpacity=0.6,
                gridWidth=0.8,
                labelColor='gray',
                labelOpacity=0.8,
                labelFontWeight=500,
                labelFontSize=12,
                labelPadding=8)


def get_text_params():
    return dict(baseline='middle', fontSize=14)


def get_title_params():
    return dict(align='left', fontSize=16, fontWeight=700)


def get_description_params():
    return dict(align='right', fontSize=10, fontWeight=500)


def get_source_label_params():
    return dict(fontSize=10, fontWeight=500, color='gray')


def get_left_align_text_params():
    return dict(align='left', dx=6, **get_text_params())


def get_right_align_text_params():
    return dict(align='right', dx=-6, **get_text_params())
