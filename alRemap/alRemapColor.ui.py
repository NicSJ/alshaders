import uigen

ui.shader({
	'name':'alRemapColor',
	'description':'Controls to adjust a color value',
	'output':'rgb',
	'maya_name':'alRemapColor',
	'maya_classification':'texture',
	'maya_id':'0x0011640D',
	'maya_swatch':True,
	'maya_matte':False,
	'maya_bump':False,
	'soft_name':'ALS_RemapColor',
	'soft_classification':'texture',
	'soft_version':1
})

ui.parameter('input', 'rgb', (0.0, 0.0, 0.0), 'Input')
ui.parameter('gamma', 'float', 1.0, 'Gamma')
ui.parameter('saturation', 'float', 1.0, 'Saturation')
ui.parameter('hueOffset', 'float', 0.0, 'Hue offset')

with uigen.group(ui, 'Contrast'):
	ui.parameter('contrast', 'float', 1.0, 'Contrast')
	ui.parameter('contrastPivot', 'float', 0.18, 'Pivot')

ui.parameter('gain', 'float', 1.0, 'Gain')
ui.parameter('exposure', 'float', 0.0, 'Exposure')
ui.parameter('mask', 'float', 1.0, 'Mask')