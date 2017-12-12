# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513106697.5132658
_enable_loop = True
_template_filename = '/Users/JessClapier/Desktop/School/IS 415/CapstoneProject/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="container">\n        <div class="row" style="height:50px;"></div>\n        <div class="row">\n            <div class="col-md-2">\n            </div>\n            <div class="col-md-8">\n                <h1 class="d-flex justify-content-center">Welcome to TwitWit &#8482;</h1>\n                <h5 class="d-flex justify-content-center">The Most Intelligent Twitter Predictor.</h5>\n\n                <span class="inputText">\n                    ')
        __M_writer(str( form ))
        __M_writer('\n                </span>\n                <h6>Load AJAX here</h6>\n            </div>\n            <div class="col-md-2">\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/Desktop/School/IS 415/CapstoneProject/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "46": 3, "53": 3, "54": 14, "55": 14, "61": 55}}
__M_END_METADATA
"""
