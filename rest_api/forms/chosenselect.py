import json
from wtforms.widgets import Select, HTMLString


class ChosenSelect(Select):

    def __init__(self, multiple=False, renderer=None, options={}):
        """
            Initiate the widget. This offers you two general options.
            First off it allows you to configure the ChosenSelect to
            allow multiple options and it allows you to pass options
            to the chosen select (this will produce a json object)
            that chosen will get passed as configuration.

                :param multiple: whether this is a multiple select
                    (default to `False`)
                :param renderer: If you do not want to use the default
                    select renderer, you can pass a function that will
                    get the field and options as arguments so that
                    you can customize the rendering.
                :param options: a dictionary of options that will
                    influence the chosen behavior. If no options are
                    given `width: 100%` will be set.
        """
        super(ChosenSelect, self).__init__(multiple=multiple)
        self.renderer = renderer
        options.setdefault('width', '100%')
        self.options = options

    def __call__(self, field, **kwargs):
        """
            Render the actual select.

                :param field: the field to render
                :param **kwargs: options to pass to the rendering
                    (i.e. class, data-* and so on)

            This will render the select as is and attach a chosen
            initiator script for the given id afterwards considering
            the options set up in the beginning.
        """
        kwargs.setdefault('id', field.id)
        # currently chosen does not reflect the readonly attribute
        # we compensate for that by automatically setting disabled,
        # if readonly if given
        # https://github.com/harvesthq/chosen/issues/67
        if kwargs.get("readonly"):
            kwargs['disabled'] = 'disabled'
        html = []
        # render the select
        if self.renderer:
            html.append(self.renderer(self, field, **kwargs))
        else:
            html.append(super(ChosenSelect, self).__call__(field, **kwargs))
        # attach the chosen initiation with options
        html.append(
            '<script>$("#%s").chosen(%s);</script>\n'
            % (kwargs['id'], json.dumps(self.options))
        )
        # return the HTML (as safe markup)
        return HTMLString('\n'.join(html))