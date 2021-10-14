from params import *
import altair as alt
import pandas as pd


def build_chart(data):
    x_label_expr = "datum.value"
    x_axis = alt.Axis(tickMinStep=10, labelExpr=x_label_expr, **get_axis_params())

    y_label_expr = "if(datum.value > 0, '+', '') + datum.label + '\u00b0' + if(datum.value == 1.2, 'C', '')"
    y_axis = alt.Axis(tickMinStep=0.2, labelExpr=y_label_expr, **get_axis_params())

    return alt.Chart(data, width=900, height=500).mark_circle(
        color='orangered',
        stroke='black',
        strokeWidth=0.7,
        size=50,
    ).encode(
        alt.X('Year', axis=x_axis, scale=get_scale(1878, 2018)),
        alt.Y('J-D', axis=y_axis, scale=get_scale(-0.5, 1.3))
    )


def build_labels_for_points(builder, marked_years):
    right_text = builder.mark_text(**get_left_align_text_params()).encode(text='Year').transform_filter(
        alt.FieldOneOfPredicate(field='Year', oneOf=marked_years['left_align']),
    )

    left_text = builder.mark_text(**get_right_align_text_params()).encode(text='Year').transform_filter(
        alt.FieldOneOfPredicate(field='Year', oneOf=marked_years['right_align']),
    )

    bold_text = builder.mark_text(fontWeight=800, **get_left_align_text_params()).encode(text='Year').transform_filter(
        alt.FieldOneOfPredicate(field='Year', oneOf=marked_years['bold']),
    )

    return left_text + right_text + bold_text


def build_line():
    return alt.Chart(pd.DataFrame({'y': [0]})).mark_rule(strokeWidth=0.3).encode(y='y')


def build_title():
    line1 = 'Annual Global Surface Temperature,'
    line2 = 'Relative to Late 19th Century Average'
    title1 = alt.Chart(_get_coord(1883, 1.2)).mark_text(text=line1, **get_title_params()).encode(x='x', y='y')
    title2 = alt.Chart(_get_coord(1883, 1.12)).mark_text(text=line2, **get_title_params()).encode(x='x', y='y')

    return title1 + title2


def build_description():
    line1 = 'Hotter than the'.upper()
    line2 = '1880-1899 average'.upper()
    line3 = 'colder'.upper()

    text1 = alt.Chart(_get_coord(2018, .15)).mark_text(text=line1, **get_description_params()).encode(x='x', y='y')
    text2 = alt.Chart(_get_coord(2018, .08)).mark_text(text=line2, **get_description_params()).encode(x='x', y='y')
    text3 = alt.Chart(_get_coord(2018, -0.08)).mark_text(text=line3, **get_description_params()).encode(x='x', y='y')

    return text1 + text2 + text3


def build_source_label():
    line = 'Source: NASA'
    return alt.Chart(_get_coord(1880, -0.7)).mark_text(text=line, **get_source_label_params()).encode(x='x', y='y')


def _get_coord(x, y):
    return pd.DataFrame({'x': [x], 'y': [y]})
