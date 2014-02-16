import uigen

ui.shader({
        'name':'alJitterColor',
        'description':'Applies random color variation within a range.',
        'output':'rgb',
        'maya_name':'alJitterColor',
        'maya_classification':'texture',
        'maya_id':'0x00116416',
        'maya_swatch':True,
        'maya_matte':False,
        'maya_bump':False,
        'soft_name':'ALS_JitterColor',
        'soft_classification':'texture',
        'soft_version':1
})

ui.parameter('input', 'rgb', (1,1,1), 'Input')

ui.parameter('minSaturation', 'float', 0.5, 'Min Saturation')
ui.parameter('maxSaturation', 'float', 1.0, 'Max Saturation')

ui.parameter('minGain', 'float', 0.5, 'Min Gain')
ui.parameter('maxGain', 'float', 1.0, 'Max Gain')

ui.parameter('minHueOffset', 'float', -0.1, 'Min Hue Offset')
ui.parameter('maxHueOffset', 'float', 0.1, 'Max Hue Offset')

ui.parameter('clamp', 'bool', True, 'Clamp')

ui.parameter('signal', 'float', 0.0, 'Signal')
