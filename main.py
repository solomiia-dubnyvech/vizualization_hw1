from source import *
from chart_builder import *


if __name__ == '__main__':
    df = load_data()
    marked_years = get_marked_years()

    chart = build_chart(df)
    line = build_line()
    text = build_labels_for_points(chart, marked_years)
    title = build_title()
    description = build_description()
    source_label = build_source_label()

    (chart + text + line + title + description + source_label).configure_view(strokeOpacity=0).show()
