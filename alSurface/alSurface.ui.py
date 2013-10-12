import uigen

ui.shader({
	'name':'alSurface',
	'description':'General-purpose, physically plausible surface shader',
	'output':'rgb',
	'maya_name':'alSurface',
	'maya_classification':'shader/surface',
	'maya_id':'0x00116402',
	'maya_swatch':True,
	'maya_matte':True,
	'maya_bump':True,
	'soft_name':'ALS_Surface',
	'soft_classification':'material',
	'soft_version':1
})

with uigen.group(ui, 'Diffuse', False):
	ui.parameter('diffuseStrength', 'float', 1.0, 'Strength', mn=0, mx=1, description='Multiplier on the diffuse result')
	ui.parameter('diffuseColor', 'rgb', (0.5, 0.5, 0.5), 'Color')
	ui.parameter('diffuseRoughness', 'float', 0.0, 'Roughness', mn=0, mx=1)

	with uigen.group(ui, 'Backlight'):
		ui.parameter('backlightStrength', 'float', 0.0, 'Strength', mn=0, mx=1)
		ui.parameter('backlightColor', 'rgb', (1.0, 1.0, 1.0), 'Color')
		ui.parameter('backlightIndirectStrength', 'float', 1.0, 'Indirect strength')

	with uigen.group(ui, 'SSS'):
		ui.parameter('sssMix', 'float', 0.0, 'Mix', mn=0, mx=1)
		ui.parameter('sssRadius', 'float', 3.6, 'Distance', mn=0)
		ui.parameter('sssRadiusColor', 'rgb', (.439, .156, .078), 'Color')
		ui.parameter('sssDensityScale', 'float', 1.0, 'Density scale', mn=0)

	with uigen.group(ui, 'Advanced'):
		ui.parameter('diffuseExtraSamples', 'int', 0, 'Extra samples', smn=-5, smx=5)
		ui.parameter('diffuseEnableCaustics', 'bool', False, 'Enable caustics')
		ui.parameter('diffuseIndirectStrength', 'float', 1.0, 'Indirect strength')
# end Diffuse

with uigen.group(ui, 'Specular 1', False):
	ui.parameter('specular1Strength', 'float', 1.0, 'Strength', mn=0, mx=1)
	ui.parameter('specular1Color', 'rgb', (1.0, 1.0, 1.0), 'Color')
	ui.parameter('specular1Roughness', 'float', 0.3, 'Roughness', mn=0, mx=1)
	ui.parameter('specular1Ior', 'float', 1.4, 'IOR', mn=1)

	with uigen.group(ui, 'Advanced'):
		ui.parameter('specular1RoughnessDepthScale', 'float', 1.5, 'Roughness depth scale', connectible=False)
		ui.parameter('specular1ExtraSamples', 'int', 0, 'Extra samples', smn=-5, smx=5)
		ui.parameter('specular1Normal', 'vector', (0.0, 0.0, 0.0), 'Normal')
		ui.parameter('specular1IndirectStrength', 'float', 1.0, 'Indirect strength')
# end Specular 1

with uigen.group(ui, 'Specular 2'):
	ui.parameter('specular2Strength', 'float', 1.0, 'Strength', mn=0, mx=1)
	ui.parameter('specular2Color', 'rgb', (1.0, 1.0, 1.0), 'Color')
	ui.parameter('specular2Roughness', 'float', 0.3, 'Roughness', mn=0, mx=1)
	ui.parameter('specular2Ior', 'float', 1.4, 'IOR', mn=1)

	with uigen.group(ui, 'Advanced'):
		ui.parameter('specular2RoughnessDepthScale', 'float', 1.5, 'Roughness depth scale', connectible=False)
		ui.parameter('specular2ExtraSamples', 'int', 0, 'Extra samples', smn=-5, smx=5)
		ui.parameter('specular2Normal', 'vector', (0.0, 0.0, 0.0), 'Normal')
		ui.parameter('specular2IndirectStrength', 'float', 1.0, 'Indirect strength')
# end Specular 2

with uigen.group(ui, 'Transmission'):
	ui.parameter('transmissionStrength', 'float', 0.0, 'Strength', mn=0, mx=1)
	ui.parameter('transmissionColor', 'rgb', (1.0, 1.0, 1.0), 'Color')
	ui.parameter('transmissionLinkToSpecular1', 'bool', True, 'Link to specular 1')
	ui.parameter('transmissionRoughness', 'float', 0.0, 'Roughness', mn=0, mx=1)
	ui.parameter('transmissionIor', 'float', 1.4, 'IOR', mn=1)

	with uigen.group(ui, 'Scattering'):
		ui.parameter('ssStrength', 'float', 0.0, 'Strength', mn=0, mx=1)
		ui.parameter('ssTargetColor', 'rgb', (.439, .156, .078), 'Color')
		ui.parameter('ssDirection', 'float', 0.0, 'Direction', mn=-1, mx=1)
		ui.parameter('ssBalance', 'float', 0.5, 'Balance', mn=0, mx=1)
		ui.parameter('ssInScattering', 'bool', False, 'In-scattering')
		ui.parameter('ssDensityScale', 'float', 1.0, 'Density scale')
		ui.parameter('ssSpecifyCoefficients', 'bool', False, 'Specify coefficients')
		ui.parameter('ssScattering', 'rgb', (1.0, 1.0, 1.0), 'Scattering')
		ui.parameter('ssAbsorption', 'rgb', (1.0, 1.0, 1.0), 'Absorption')

	with uigen.group(ui, 'Advanced'):
		ui.parameter('transmissionRoughnessDepthScale', 'float', 1.4, 'Roughness depth scale')
		ui.parameter('transmissionExtraSamples', 'int', 0, 'Extra samples', smn=-5, smx=5)
		ui.parameter('transmissionEnableCaustics', 'bool', True, 'Enable internal reflections')
		ui.parameter('rrTransmission', 'bool', False, 'RR')
		ui.parameter('rrTransmissionDepth', 'int', 1, 'RR depth')
# end Transmission

with uigen.group(ui, 'Emission'):
	ui.parameter('emissionStrength', 'float', 0.0, 'Strength', mn=0)
	ui.parameter('emissionTargetColor', 'rgb', (1.0, 1.0, 1.0), 'Color')
# end Emission

with uigen.group(ui, 'IDs'):
	for i in range(1,9):
		ui.parameter('id%d'%i, 'rgb', (0.0, 0.0, 0.0))
# end IDs

with uigen.group(ui, 'AOVs'):
	ui.parameter('lightGroupsIndirect', 'bool', False, 'Indirect light groups')
	ui.parameter('standardCompatibleAOVs', 'bool', False, 'Write standard AOVs only')
	ui.parameter('transmitAovs', 'bool', False, 'Transmit AOVs')
	ui.aov('aov_diffuse_color', 'rgb', 'Diffuse color')
	ui.aov('aov_direct_diffuse', 'rgb', 'Direct diffuse')
	ui.aov('aov_direct_diffuse_raw', 'rgb', 'Direct diffuse (raw)')
	ui.aov('aov_indirect_diffuse', 'rgb', 'Indirect diffuse')
	ui.aov('aov_indirect_diffuse_raw', 'rgb', 'Indirect diffuse (raw)')
	ui.aov('aov_direct_backlight', 'rgb', 'Direct backlight')
	ui.aov('aov_indirect_backlight', 'rgb', 'Indirect backlight')
	ui.aov('aov_direct_specular', 'rgb', 'Direct specular')
	ui.aov('aov_indirect_specular', 'rgb', 'Indirect specular')
	ui.aov('aov_direct_specular_2', 'rgb', 'Direct specular 2')
	ui.aov('aov_indirect_specular_2', 'rgb', 'Indirect specular 2')
	ui.aov('aov_single_scatter', 'rgb', 'Single scatter')
	ui.aov('aov_sss', 'rgb', 'SSS')
	ui.aov('aov_refraction', 'rgb', 'Refraction')
	ui.aov('aov_emission', 'rgb', 'Emission')
	ui.aov('aov_uv', 'rgb', 'UV')
	ui.aov('aov_depth', 'rgb', 'Depth')
	ui.aov('aov_light_group_1', 'rgb', 'Light group [1]')
	ui.aov('aov_light_group_2', 'rgb', 'Light group [2]')
	ui.aov('aov_light_group_3', 'rgb', 'Light group [3]')
	ui.aov('aov_light_group_4', 'rgb', 'Light group [4]')
	ui.aov('aov_light_group_5', 'rgb', 'Light group [5]')
	ui.aov('aov_light_group_6', 'rgb', 'Light group [6]')
	ui.aov('aov_light_group_7', 'rgb', 'Light group [7]')
	ui.aov('aov_light_group_8', 'rgb', 'Light group [8]')
	ui.aov('aov_id_1', 'rgb', 'ID [1]')
	ui.aov('aov_id_2', 'rgb', 'ID [2]')
	ui.aov('aov_id_3', 'rgb', 'ID [3]')
	ui.aov('aov_id_4', 'rgb', 'ID [4]')
	ui.aov('aov_id_5', 'rgb', 'ID [5]')
	ui.aov('aov_id_6', 'rgb', 'ID [6]')
	ui.aov('aov_id_7', 'rgb', 'ID [7]')
	ui.aov('aov_id_8', 'rgb', 'ID [8]')




