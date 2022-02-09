"""
    htmlx.x3d
    ====================================
    Generate x3d with python 3

"""

from htmlx.dom import Element
from htmlx.html import closed_tag

x3d = X3D = type("x3d", (Element,), {"name": "x3d"})
scene = Scene = type("scene", (Element,), {"name": "scene"})
material = Material = type("material", (Element,), {"name": "material"})
appearance = Appearance = type("appearance", (Element,), {"name": "appearance"})
sphere = Sphere = type("sphere", (Element,), {"name": "sphere"})
shape = Shape = type("shape", (Element,), {"name": "shape"})
transform = Transform = type("transform", (Element,), {"name": "transform"})
timeSensor = TimeSensor = type("timeSensor", (Element,), {"name": "timeSensor"})
inline = Inline = type("inline", (Element,), {"name": "inline"})
box = Box = type("box", (Element,), {"name": "box"})
plane = Plane = type("plane", (Element,), {"name": "plane"})

# TODO - go through examples to find which are usually lower. i.e before they allowed mised cases
positionInterpolator = PositionInterpolator = type(
    "PositionInterpolator", (Element,), {"name": "PositionInterpolator"}
)
route = Route = type("Route", (Element,), {"name": "Route"})
anchor = Anchor = type("Anchor", (Element,), {"name": "Anchor"})
arc2D = Arc2D = type("Arc2D", (Element,), {"name": "Arc2D"})
arcClose2D = ArcClose2D = type("ArcClose2D", (Element,), {"name": "ArcClose2D"})
audioClip = AudioClip = type("AudioClip", (Element,), {"name": "AudioClip"})
background = Background = type("Background", (Element,), {"name": "Background"})
ballJoint = BallJoint = type("BallJoint", (Element,), {"name": "BallJoint"})
billboard = Billboard = type("Billboard", (Element,), {"name": "Billboard"})
binaryGeometry = BinaryGeometry = type(
    "BinaryGeometry", (Element,), {"name": "BinaryGeometry"}
)
blendedVolumeStyle = BlendedVolumeStyle = type(
    "BlendedVolumeStyle", (Element,), {"name": "BlendedVolumeStyle"}
)
blendMode = BlendMode = type("BlendMode", (Element,), {"name": "BlendMode"})
block = Block = type("Block", (Element,), {"name": "Block"})
boundaryEnhancementVolumeStyle = BoundaryEnhancementVolumeStyle = type(
    "BoundaryEnhancementVolumeStyle",
    (Element,),
    {"name": "BoundaryEnhancementVolumeStyle"},
)
bufferAccessor = BufferAccessor = type(
    "BufferAccessor", (Element,), {"name": "BufferAccessor"}
)
bufferGeometry = BufferGeometry = type(
    "BufferGeometry", (Element,), {"name": "BufferGeometry"}
)
bufferView = BufferView = type("BufferView", (Element,), {"name": "BufferView"})
cADAssembly = CADAssembly = type("CADAssembly", (Element,), {"name": "CADAssembly"})
cADFace = CADFace = type("CADFace", (Element,), {"name": "CADFace"})
cADLayer = CADLayer = type("CADLayer", (Element,), {"name": "CADLayer"})
cADPart = CADPart = type("CADPart", (Element,), {"name": "CADPart"})
cartoonVolumeStyle = CartoonVolumeStyle = type(
    "CartoonVolumeStyle", (Element,), {"name": "CartoonVolumeStyle"}
)
circle2D = Circle2D = type("Circle2D", (Element,), {"name": "Circle2D"})
clipPlane = ClipPlane = type("ClipPlane", (Element,), {"name": "ClipPlane"})
collidableShape = CollidableShape = type(
    "CollidableShape", (Element,), {"name": "CollidableShape"}
)
collision = Collision = type("Collision", (Element,), {"name": "Collision"})
collisionCollection = CollisionCollection = type(
    "CollisionCollection", (Element,), {"name": "CollisionCollection"}
)
collisionSensor = CollisionSensor = type(
    "CollisionSensor", (Element,), {"name": "CollisionSensor"}
)
color = Color = type("Color", (Element,), {"name": "Color"})
colorChaser = ColorChaser = type("ColorChaser", (Element,), {"name": "ColorChaser"})
colorDamper = ColorDamper = type("ColorDamper", (Element,), {"name": "ColorDamper"})
colorInterpolator = ColorInterpolator = type(
    "ColorInterpolator", (Element,), {"name": "ColorInterpolator"}
)
colorMaskMode = ColorMaskMode = type(
    "ColorMaskMode", (Element,), {"name": "ColorMaskMode"}
)
colorRGBA = ColorRGBA = type("ColorRGBA", (Element,), {"name": "ColorRGBA"})
commonSurfaceShader = CommonSurfaceShader = type(
    "CommonSurfaceShader", (Element,), {"name": "CommonSurfaceShader"}
)
composedCubeMapTexture = ComposedCubeMapTexture = type(
    "ComposedCubeMapTexture", (Element,), {"name": "ComposedCubeMapTexture"}
)
composedShader = ComposedShader = type(
    "ComposedShader", (Element,), {"name": "ComposedShader"}
)
composedTexture3D = ComposedTexture3D = type(
    "ComposedTexture3D", (Element,), {"name": "ComposedTexture3D"}
)
composedVolumeStyle = ComposedVolumeStyle = type(
    "ComposedVolumeStyle", (Element,), {"name": "ComposedVolumeStyle"}
)
cone = Cone = type("Cone", (Element,), {"name": "Cone"})
coordinate = Coordinate = type("Coordinate", (Element,), {"name": "Coordinate"})
coordinateDamper = CoordinateDamper = type(
    "CoordinateDamper", (Element,), {"name": "CoordinateDamper"}
)
coordinateDouble = CoordinateDouble = type(
    "CoordinateDouble", (Element,), {"name": "CoordinateDouble"}
)
coordinateInterpolator = CoordinateInterpolator = type(
    "CoordinateInterpolator", (Element,), {"name": "CoordinateInterpolator"}
)
cylinder = Cylinder = type("Cylinder", (Element,), {"name": "Cylinder"})
cylinderSensor = CylinderSensor = type(
    "CylinderSensor", (Element,), {"name": "CylinderSensor"}
)
depthMode = DepthMode = type("DepthMode", (Element,), {"name": "DepthMode"})
directionalLight = DirectionalLight = type(
    "DirectionalLight", (Element,), {"name": "DirectionalLight"}
)
dish = Dish = type("Dish", (Element,), {"name": "Dish"})
disk2D = Disk2D = type("Disk2D", (Element,), {"name": "Disk2D"})
doubleAxisHingeJoint = DoubleAxisHingeJoint = type(
    "DoubleAxisHingeJoint", (Element,), {"name": "DoubleAxisHingeJoint"}
)
dynamicLOD = DynamicLOD = type("DynamicLOD", (Element,), {"name": "DynamicLOD"})
edgeEnhancementVolumeStyle = EdgeEnhancementVolumeStyle = type(
    "EdgeEnhancementVolumeStyle", (Element,), {"name": "EdgeEnhancementVolumeStyle"}
)
elevationGrid = ElevationGrid = type(
    "ElevationGrid", (Element,), {"name": "ElevationGrid"}
)
environment = Environment = type("Environment", (Element,), {"name": "Environment"})
extrusion = Extrusion = type("Extrusion", (Element,), {"name": "Extrusion"})
field = Field = type("Field", (Element,), {"name": "Field"})
floatVertexAttribute = FloatVertexAttribute = type(
    "FloatVertexAttribute", (Element,), {"name": "FloatVertexAttribute"}
)
fog = Fog = type("Fog", (Element,), {"name": "Fog"})
fontStyle = FontStyle = type("FontStyle", (Element,), {"name": "FontStyle"})
generatedCubeMapTexture = GeneratedCubeMapTexture = type(
    "GeneratedCubeMapTexture", (Element,), {"name": "GeneratedCubeMapTexture"}
)
geoCoordinate = GeoCoordinate = type(
    "GeoCoordinate", (Element,), {"name": "GeoCoordinate"}
)
geoElevationGrid = GeoElevationGrid = type(
    "GeoElevationGrid", (Element,), {"name": "GeoElevationGrid"}
)
geoLocation = GeoLocation = type("GeoLocation", (Element,), {"name": "GeoLocation"})
geoLOD = GeoLOD = type("GeoLOD", (Element,), {"name": "GeoLOD"})
geoMetadata = GeoMetadata = type("GeoMetadata", (Element,), {"name": "GeoMetadata"})
geoOrigin = GeoOrigin = type("GeoOrigin", (Element,), {"name": "GeoOrigin"})
geoPositionInterpolator = GeoPositionInterpolator = type(
    "GeoPositionInterpolator", (Element,), {"name": "GeoPositionInterpolator"}
)
geoTransform = GeoTransform = type("GeoTransform", (Element,), {"name": "GeoTransform"})
geoViewpoint = GeoViewpoint = type("GeoViewpoint", (Element,), {"name": "GeoViewpoint"})
group = Group = type("Group", (Element,), {"name": "Group"})
hAnimDisplacer = HAnimDisplacer = type(
    "HAnimDisplacer", (Element,), {"name": "HAnimDisplacer"}
)
hAnimHumanoid = HAnimHumanoid = type(
    "HAnimHumanoid", (Element,), {"name": "HAnimHumanoid"}
)
hAnimJoint = HAnimJoint = type("HAnimJoint", (Element,), {"name": "HAnimJoint"})
hAnimSegment = HAnimSegment = type("HAnimSegment", (Element,), {"name": "HAnimSegment"})
hAnimSite = HAnimSite = type("HAnimSite", (Element,), {"name": "HAnimSite"})
imageTexture = ImageTexture = type("ImageTexture", (Element,), {"name": "ImageTexture"})
imageTexture3D = ImageTexture3D = type(
    "ImageTexture3D", (Element,), {"name": "ImageTexture3D"}
)
imageTextureAtlas = ImageTextureAtlas = type(
    "ImageTextureAtlas", (Element,), {"name": "ImageTextureAtlas"}
)
indexedFaceSet = IndexedFaceSet = type(
    "IndexedFaceSet", (Element,), {"name": "IndexedFaceSet"}
)
indexedLineSet = IndexedLineSet = type(
    "IndexedLineSet", (Element,), {"name": "IndexedLineSet"}
)
indexedQuadSet = IndexedQuadSet = type(
    "IndexedQuadSet", (Element,), {"name": "IndexedQuadSet"}
)
indexedTriangleSet = IndexedTriangleSet = type(
    "IndexedTriangleSet", (Element,), {"name": "IndexedTriangleSet"}
)
indexedTriangleStripSet = IndexedTriangleStripSet = type(
    "IndexedTriangleStripSet", (Element,), {"name": "IndexedTriangleStripSet"}
)
isoSurfaceVolumeData = IsoSurfaceVolumeData = type(
    "IsoSurfaceVolumeData", (Element,), {"name": "IsoSurfaceVolumeData"}
)
lineProperties = LineProperties = type(
    "LineProperties", (Element,), {"name": "LineProperties"}
)
lineSet = LineSet = type("LineSet", (Element,), {"name": "LineSet"})
lOD = LOD = type("LOD", (Element,), {"name": "LOD"})
matrixTextureTransform = MatrixTextureTransform = type(
    "MatrixTextureTransform", (Element,), {"name": "MatrixTextureTransform"}
)
matrixTransform = MatrixTransform = type(
    "MatrixTransform", (Element,), {"name": "MatrixTransform"}
)
mesh = Mesh = type("Mesh", (Element,), {"name": "Mesh"})
metadataBoolean = MetadataBoolean = type(
    "MetadataBoolean", (Element,), {"name": "MetadataBoolean"}
)
metadataDouble = MetadataDouble = type(
    "MetadataDouble", (Element,), {"name": "MetadataDouble"}
)
metadataFloat = MetadataFloat = type(
    "MetadataFloat", (Element,), {"name": "MetadataFloat"}
)
metadataInteger = MetadataInteger = type(
    "MetadataInteger", (Element,), {"name": "MetadataInteger"}
)
metadataSet = MetadataSet = type("MetadataSet", (Element,), {"name": "MetadataSet"})
metadataString = MetadataString = type(
    "MetadataString", (Element,), {"name": "MetadataString"}
)
motorJoint = MotorJoint = type("MotorJoint", (Element,), {"name": "MotorJoint"})
movieTexture = MovieTexture = type("MovieTexture", (Element,), {"name": "MovieTexture"})
mPRPlane = MPRPlane = type("MPRPlane", (Element,), {"name": "MPRPlane"})
mPRVolumeStyle = MPRVolumeStyle = type(
    "MPRVolumeStyle", (Element,), {"name": "MPRVolumeStyle"}
)
multiTexture = MultiTexture = type("MultiTexture", (Element,), {"name": "MultiTexture"})
multiTextureCoordinate = MultiTextureCoordinate = type(
    "MultiTextureCoordinate", (Element,), {"name": "MultiTextureCoordinate"}
)
navigationInfo = NavigationInfo = type(
    "NavigationInfo", (Element,), {"name": "NavigationInfo"}
)
normal = Normal = type("Normal", (Element,), {"name": "Normal"})
normalInterpolator = NormalInterpolator = type(
    "NormalInterpolator", (Element,), {"name": "NormalInterpolator"}
)
nozzle = Nozzle = type("Nozzle", (Element,), {"name": "Nozzle"})
opacityMapVolumeStyle = OpacityMapVolumeStyle = type(
    "OpacityMapVolumeStyle", (Element,), {"name": "OpacityMapVolumeStyle"}
)
orientationChaser = OrientationChaser = type(
    "OrientationChaser", (Element,), {"name": "OrientationChaser"}
)
orientationDamper = OrientationDamper = type(
    "OrientationDamper", (Element,), {"name": "OrientationDamper"}
)
orientationInterpolator = OrientationInterpolator = type(
    "OrientationInterpolator", (Element,), {"name": "OrientationInterpolator"}
)
orthoViewpoint = OrthoViewpoint = type(
    "OrthoViewpoint", (Element,), {"name": "OrthoViewpoint"}
)
param = Param = type("Param", (Element,), {"name": "Param"})
particleSet = ParticleSet = type("ParticleSet", (Element,), {"name": "ParticleSet"})
physicalEnvironmentLight = PhysicalEnvironmentLight = type(
    "PhysicalEnvironmentLight", (Element,), {"name": "PhysicalEnvironmentLight"}
)
physicalMaterial = PhysicalMaterial = type(
    "PhysicalMaterial", (Element,), {"name": "PhysicalMaterial"}
)
pixelTexture = PixelTexture = type("PixelTexture", (Element,), {"name": "PixelTexture"})
pixelTexture3D = PixelTexture3D = type(
    "PixelTexture3D", (Element,), {"name": "PixelTexture3D"}
)
planeSensor = PlaneSensor = type("PlaneSensor", (Element,), {"name": "PlaneSensor"})
pointLight = PointLight = type("PointLight", (Element,), {"name": "PointLight"})
pointSet = PointSet = type("PointSet", (Element,), {"name": "PointSet"})
polyline2D = Polyline2D = type("Polyline2D", (Element,), {"name": "Polyline2D"})
polypoint2D = Polypoint2D = type("Polypoint2D", (Element,), {"name": "Polypoint2D"})
popGeometry = PopGeometry = type("PopGeometry", (Element,), {"name": "PopGeometry"})
popGeometryLevel = PopGeometryLevel = type(
    "PopGeometryLevel", (Element,), {"name": "PopGeometryLevel"}
)
positionChaser = PositionChaser = type(
    "PositionChaser", (Element,), {"name": "PositionChaser"}
)
positionChaser2D = PositionChaser2D = type(
    "PositionChaser2D", (Element,), {"name": "PositionChaser2D"}
)
positionDamper = PositionDamper = type(
    "PositionDamper", (Element,), {"name": "PositionDamper"}
)
positionDamper2D = PositionDamper2D = type(
    "PositionDamper2D", (Element,), {"name": "PositionDamper2D"}
)
positionInterpolator = PositionInterpolator = type(
    "PositionInterpolator", (Element,), {"name": "PositionInterpolator"}
)
positionInterpolator2D = PositionInterpolator2D = type(
    "PositionInterpolator2D", (Element,), {"name": "PositionInterpolator2D"}
)
projectionVolumeStyle = ProjectionVolumeStyle = type(
    "ProjectionVolumeStyle", (Element,), {"name": "ProjectionVolumeStyle"}
)
pyramid = Pyramid = type("Pyramid", (Element,), {"name": "Pyramid"})
quadSet = QuadSet = type("QuadSet", (Element,), {"name": "QuadSet"})
radarVolumeStyle = RadarVolumeStyle = type(
    "RadarVolumeStyle", (Element,), {"name": "RadarVolumeStyle"}
)
rectangle2D = Rectangle2D = type("Rectangle2D", (Element,), {"name": "Rectangle2D"})
rectangularTorus = RectangularTorus = type(
    "RectangularTorus", (Element,), {"name": "RectangularTorus"}
)
refinementTexture = RefinementTexture = type(
    "RefinementTexture", (Element,), {"name": "RefinementTexture"}
)
remoteSelectionGroup = RemoteSelectionGroup = type(
    "RemoteSelectionGroup", (Element,), {"name": "RemoteSelectionGroup"}
)
renderedTexture = RenderedTexture = type(
    "RenderedTexture", (Element,), {"name": "RenderedTexture"}
)
rigidBody = RigidBody = type("RigidBody", (Element,), {"name": "RigidBody"})
rigidBodyCollection = RigidBodyCollection = type(
    "RigidBodyCollection", (Element,), {"name": "RigidBodyCollection"}
)
scalarChaser = ScalarChaser = type("ScalarChaser", (Element,), {"name": "ScalarChaser"})
scalarDamper = ScalarDamper = type("ScalarDamper", (Element,), {"name": "ScalarDamper"})
scalarInterpolator = ScalarInterpolator = type(
    "ScalarInterpolator", (Element,), {"name": "ScalarInterpolator"}
)
segmentedVolumeData = SegmentedVolumeData = type(
    "SegmentedVolumeData", (Element,), {"name": "SegmentedVolumeData"}
)
shadedVolumeStyle = ShadedVolumeStyle = type(
    "ShadedVolumeStyle", (Element,), {"name": "ShadedVolumeStyle"}
)
shaderPart = ShaderPart = type("ShaderPart", (Element,), {"name": "ShaderPart"})
silhouetteEnhancementVolumeStyle = SilhouetteEnhancementVolumeStyle = type(
    "SilhouetteEnhancementVolumeStyle",
    (Element,),
    {"name": "SilhouetteEnhancementVolumeStyle"},
)
singleAxisHingeJoint = SingleAxisHingeJoint = type(
    "SingleAxisHingeJoint", (Element,), {"name": "SingleAxisHingeJoint"}
)
sliderJoint = SliderJoint = type("SliderJoint", (Element,), {"name": "SliderJoint"})
slopedCylinder = SlopedCylinder = type(
    "SlopedCylinder", (Element,), {"name": "SlopedCylinder"}
)
snout = Snout = type("Snout", (Element,), {"name": "Snout"})
solidOfRevolution = SolidOfRevolution = type(
    "SolidOfRevolution", (Element,), {"name": "SolidOfRevolution"}
)
sound = Sound = type("Sound", (Element,), {"name": "Sound"})
sphereSegment = SphereSegment = type(
    "SphereSegment", (Element,), {"name": "SphereSegment"}
)
sphereSensor = SphereSensor = type("SphereSensor", (Element,), {"name": "SphereSensor"})
splinePositionInterpolator = SplinePositionInterpolator = type(
    "SplinePositionInterpolator", (Element,), {"name": "SplinePositionInterpolator"}
)
spotLight = SpotLight = type("SpotLight", (Element,), {"name": "SpotLight"})
staticGroup = StaticGroup = type("StaticGroup", (Element,), {"name": "StaticGroup"})
stippleVolumeStyle = StippleVolumeStyle = type(
    "StippleVolumeStyle", (Element,), {"name": "StippleVolumeStyle"}
)
surfaceShaderTexture = SurfaceShaderTexture = type(
    "SurfaceShaderTexture", (Element,), {"name": "SurfaceShaderTexture"}
)
switch = Switch = type("Switch", (Element,), {"name": "Switch"})
texCoordDamper2D = TexCoordDamper2D = type(
    "TexCoordDamper2D", (Element,), {"name": "TexCoordDamper2D"}
)
text = Text = type("Text", (Element,), {"name": "Text"})
texture = Texture = type("Texture", (Element,), {"name": "Texture"})
textureCoordinate = TextureCoordinate = type(
    "TextureCoordinate", (Element,), {"name": "TextureCoordinate"}
)
textureCoordinate3D = TextureCoordinate3D = type(
    "TextureCoordinate3D", (Element,), {"name": "TextureCoordinate3D"}
)
textureCoordinateGenerator = TextureCoordinateGenerator = type(
    "TextureCoordinateGenerator", (Element,), {"name": "TextureCoordinateGenerator"}
)
textureProperties = TextureProperties = type(
    "TextureProperties", (Element,), {"name": "TextureProperties"}
)
textureTransform = TextureTransform = type(
    "TextureTransform", (Element,), {"name": "TextureTransform"}
)
textureTransform3D = TextureTransform3D = type(
    "TextureTransform3D", (Element,), {"name": "TextureTransform3D"}
)
textureTransformMatrix3D = TextureTransformMatrix3D = type(
    "TextureTransformMatrix3D", (Element,), {"name": "TextureTransformMatrix3D"}
)
toneMappedVolumeStyle = ToneMappedVolumeStyle = type(
    "ToneMappedVolumeStyle", (Element,), {"name": "ToneMappedVolumeStyle"}
)
torus = Torus = type("Torus", (Element,), {"name": "Torus"})
touchSensor = TouchSensor = type("TouchSensor", (Element,), {"name": "TouchSensor"})
triangleSet = TriangleSet = type("TriangleSet", (Element,), {"name": "TriangleSet"})
triangleSet2D = TriangleSet2D = type(
    "TriangleSet2D", (Element,), {"name": "TriangleSet2D"}
)
twoSidedMaterial = TwoSidedMaterial = type(
    "TwoSidedMaterial", (Element,), {"name": "TwoSidedMaterial"}
)
uniform = Uniform = type("Uniform", (Element,), {"name": "Uniform"})
universalJoint = UniversalJoint = type(
    "UniversalJoint", (Element,), {"name": "UniversalJoint"}
)
viewfrustum = Viewfrustum = type("Viewfrustum", (Element,), {"name": "Viewfrustum"})
viewpoint = Viewpoint = type("Viewpoint", (Element,), {"name": "Viewpoint"})
volumeData = VolumeData = type("VolumeData", (Element,), {"name": "VolumeData"})
worldInfo = WorldInfo = type("WorldInfo", (Element,), {"name": "WorldInfo"})
x3DAppearanceChildNode = X3DAppearanceChildNode = type(
    "X3DAppearanceChildNode", (Element,), {"name": "X3DAppearanceChildNode"}
)
x3DAppearanceNode = X3DAppearanceNode = type(
    "X3DAppearanceNode", (Element,), {"name": "X3DAppearanceNode"}
)
x3DBackgroundNode = X3DBackgroundNode = type(
    "X3DBackgroundNode", (Element,), {"name": "X3DBackgroundNode"}
)
x3DBinaryContainerGeometryNode = X3DBinaryContainerGeometryNode = type(
    "X3DBinaryContainerGeometryNode",
    (Element,),
    {"name": "X3DBinaryContainerGeometryNode"},
)
x3DBindableNode = X3DBindableNode = type(
    "X3DBindableNode", (Element,), {"name": "X3DBindableNode"}
)
x3DBoundedObject = X3DBoundedObject = type(
    "X3DBoundedObject", (Element,), {"name": "X3DBoundedObject"}
)
x3DChaserNode = X3DChaserNode = type(
    "X3DChaserNode", (Element,), {"name": "X3DChaserNode"}
)
x3DChildNode = X3DChildNode = type("X3DChildNode", (Element,), {"name": "X3DChildNode"})
x3DColorNode = X3DColorNode = type("X3DColorNode", (Element,), {"name": "X3DColorNode"})
x3DComposableVolumeRenderStyleNode = X3DComposableVolumeRenderStyleNode = type(
    "X3DComposableVolumeRenderStyleNode",
    (Element,),
    {"name": "X3DComposableVolumeRenderStyleNode"},
)
x3DComposedGeometryNode = X3DComposedGeometryNode = type(
    "X3DComposedGeometryNode", (Element,), {"name": "X3DComposedGeometryNode"}
)
x3DCoordinateNode = X3DCoordinateNode = type(
    "X3DCoordinateNode", (Element,), {"name": "X3DCoordinateNode"}
)
x3DDamperNode = X3DDamperNode = type(
    "X3DDamperNode", (Element,), {"name": "X3DDamperNode"}
)
x3DDragSensorNode = X3DDragSensorNode = type(
    "X3DDragSensorNode", (Element,), {"name": "X3DDragSensorNode"}
)
x3DEnvironmentNode = X3DEnvironmentNode = type(
    "X3DEnvironmentNode", (Element,), {"name": "X3DEnvironmentNode"}
)
x3DEnvironmentTextureNode = X3DEnvironmentTextureNode = type(
    "X3DEnvironmentTextureNode", (Element,), {"name": "X3DEnvironmentTextureNode"}
)
x3DFogNode = X3DFogNode = type("X3DFogNode", (Element,), {"name": "X3DFogNode"})
x3DFollowerNode = X3DFollowerNode = type(
    "X3DFollowerNode", (Element,), {"name": "X3DFollowerNode"}
)
x3DFontStyleNode = X3DFontStyleNode = type(
    "X3DFontStyleNode", (Element,), {"name": "X3DFontStyleNode"}
)
x3DGeometricPropertyNode = X3DGeometricPropertyNode = type(
    "X3DGeometricPropertyNode", (Element,), {"name": "X3DGeometricPropertyNode"}
)
x3DGeometryNode = X3DGeometryNode = type(
    "X3DGeometryNode", (Element,), {"name": "X3DGeometryNode"}
)
x3DGroupingNode = X3DGroupingNode = type(
    "X3DGroupingNode", (Element,), {"name": "X3DGroupingNode"}
)
x3DInfoNode = X3DInfoNode = type("X3DInfoNode", (Element,), {"name": "X3DInfoNode"})
x3DInterpolatorNode = X3DInterpolatorNode = type(
    "X3DInterpolatorNode", (Element,), {"name": "X3DInterpolatorNode"}
)
x3DLightNode = X3DLightNode = type("X3DLightNode", (Element,), {"name": "X3DLightNode"})
x3DLODNode = X3DLODNode = type("X3DLODNode", (Element,), {"name": "X3DLODNode"})
x3DMaterialNode = X3DMaterialNode = type(
    "X3DMaterialNode", (Element,), {"name": "X3DMaterialNode"}
)
x3DMetadataObject = X3DMetadataObject = type(
    "X3DMetadataObject", (Element,), {"name": "X3DMetadataObject"}
)
x3DNavigationInfoNode = X3DNavigationInfoNode = type(
    "X3DNavigationInfoNode", (Element,), {"name": "X3DNavigationInfoNode"}
)
x3DNBodyCollidableNode = X3DNBodyCollidableNode = type(
    "X3DNBodyCollidableNode", (Element,), {"name": "X3DNBodyCollidableNode"}
)
x3DNode = X3DNode = type("X3DNode", (Element,), {"name": "X3DNode"})
x3DPlanarGeometryNode = X3DPlanarGeometryNode = type(
    "X3DPlanarGeometryNode", (Element,), {"name": "X3DPlanarGeometryNode"}
)
x3DPointingDeviceSensorNode = X3DPointingDeviceSensorNode = type(
    "X3DPointingDeviceSensorNode", (Element,), {"name": "X3DPointingDeviceSensorNode"}
)
x3DRigidJointNode = X3DRigidJointNode = type(
    "X3DRigidJointNode", (Element,), {"name": "X3DRigidJointNode"}
)
x3DSensorNode = X3DSensorNode = type(
    "X3DSensorNode", (Element,), {"name": "X3DSensorNode"}
)
x3DShaderNode = X3DShaderNode = type(
    "X3DShaderNode", (Element,), {"name": "X3DShaderNode"}
)
x3DShapeNode = X3DShapeNode = type("X3DShapeNode", (Element,), {"name": "X3DShapeNode"})
x3DSoundNode = X3DSoundNode = type("X3DSoundNode", (Element,), {"name": "X3DSoundNode"})
x3DSoundSourceNode = X3DSoundSourceNode = type(
    "X3DSoundSourceNode", (Element,), {"name": "X3DSoundSourceNode"}
)
x3DSpatialGeometryNode = X3DSpatialGeometryNode = type(
    "X3DSpatialGeometryNode", (Element,), {"name": "X3DSpatialGeometryNode"}
)
x3DTexture3DNode = X3DTexture3DNode = type(
    "X3DTexture3DNode", (Element,), {"name": "X3DTexture3DNode"}
)
x3DTextureCoordinateNode = X3DTextureCoordinateNode = type(
    "X3DTextureCoordinateNode", (Element,), {"name": "X3DTextureCoordinateNode"}
)
x3DTextureNode = X3DTextureNode = type(
    "X3DTextureNode", (Element,), {"name": "X3DTextureNode"}
)
x3DTextureTransformNode = X3DTextureTransformNode = type(
    "X3DTextureTransformNode", (Element,), {"name": "X3DTextureTransformNode"}
)
x3DTimeDependentNode = X3DTimeDependentNode = type(
    "X3DTimeDependentNode", (Element,), {"name": "X3DTimeDependentNode"}
)
x3DTouchSensorNode = X3DTouchSensorNode = type(
    "X3DTouchSensorNode", (Element,), {"name": "X3DTouchSensorNode"}
)
x3DTransformNode = X3DTransformNode = type(
    "X3DTransformNode", (Element,), {"name": "X3DTransformNode"}
)
x3DVertexAttributeNode = X3DVertexAttributeNode = type(
    "X3DVertexAttributeNode", (Element,), {"name": "X3DVertexAttributeNode"}
)
x3DViewpointNode = X3DViewpointNode = type(
    "X3DViewpointNode", (Element,), {"name": "X3DViewpointNode"}
)
x3DVolumeDataNode = X3DVolumeDataNode = type(
    "X3DVolumeDataNode", (Element,), {"name": "X3DVolumeDataNode"}
)
x3DVolumeRenderStyleNode = X3DVolumeRenderStyleNode = type(
    "X3DVolumeRenderStyleNode", (Element,), {"name": "X3DVolumeRenderStyleNode"}
)
