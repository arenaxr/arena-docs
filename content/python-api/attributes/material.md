---
title: arena.attributes.material
parent: arena.attributes
grand_parent: Python API
---
<small>arena-py API <a href="https://github.com/arenaxr/arena-py/blob/v0.11.0/arena">v0.11.0</a></small>
<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
<a href="./../arena.html">arena</a><wbr>.<a href="./../attributes.html">attributes</a><wbr>.material    </h1>

                
                
                
                
            </section>
                <section id="Material">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Material</span><wbr>(<span class="base"><a href="attribute.html#Attribute">arena.attributes.attribute.Attribute</a></span>):

        
    </div>
    <a class="headerlink" href="#Material"></a>
    
            <div class="docstring"><p>Material attribute class to manage its properties in the ARENA: The material properties of the object's surface. More properties at <a href="https://aframe.io/docs/1.5.0/components/material.html">https://aframe.io/docs/1.5.0/components/material.html</a> A-Frame Material.
Usage: <code>material=Material(...)</code></p>

<h6 id="parameters">Parameters</h6>

<ul>
<li><strong>float alphaTest</strong>:  Alpha test threshold for transparency. Defaults to '0' (optional)</li>
<li><strong>float anisotropy</strong>:  The anisotropic filtering sample rate to use for the textures. A value of 0 means the default value will be used, see renderer. Defaults to '0' (optional)</li>
<li><strong>str blending</strong>:  The blending mode for the material's RGB and Alpha sent to the WebGLRenderer. Allows [none, normal, additive, subtractive, multiply] Defaults to 'normal' (optional)</li>
<li><strong>str color</strong>:  Base diffuse color. Defaults to '#ffffff' (optional)</li>
<li><strong>str combine: How the environment map mixes with the material. Requires shader</strong>:  phong. Allows [mix, add, multiply] Defaults to 'mix' (optional)</li>
<li><strong>bool depthTest</strong>:  Whether depth testing is enabled when rendering the material. Defaults to 'True' (optional)</li>
<li><strong>bool depthWrite</strong>:  Render when depth test succeeds. Defaults to 'True' (optional)</li>
<li><strong>bool dithering</strong>:  Whether material is dithered with noise. Removes banding from gradients like ones produced by lighting. Defaults to 'True' (optional)</li>
<li><strong>str emissive: The color of the emissive lighting component. Used to make objects produce light even without other lighting in the scene. Requires shader</strong>:  standard or phong Defaults to '#000000' (optional)</li>
<li><strong>float emissiveIntensity: Intensity of the emissive lighting component. Requires shader</strong>:  standard or phong Defaults to '1' (optional)</li>
<li><strong>bool flatShading</strong>:  Use THREE.FlatShading rather than THREE.StandardShading. Defaults to 'False' (optional)</li>
<li><strong>bool fog</strong>:  Whether or not material is affected by fog. Defaults to 'True' (optional)</li>
<li><strong>int height: Height of video (in pixels), if defining a video texture. Requires shader</strong>:  standard or flat. Defaults to '256' (optional)</li>
<li><strong>float metalness: How metallic the material is from 0 to 1. Requires shader</strong>:  standard. Defaults to '0' (optional)</li>
<li><strong>bool npot</strong>:  Use settings for non-power-of-two (NPOT) texture. Defaults to 'False' (optional)</li>
<li><strong>dict offset: Texture offset to be used. Defaults to '{'x': 0, 'y'</strong>:  0}' (optional)</li>
<li><strong>float opacity</strong>:  Extent of transparency. If the transparent property is not true, then the material will remain opaque and opacity will only affect color. Defaults to '1' (optional)</li>
<li><strong>float reflectivity: How much the environment map affects the surface. Requires shader</strong>:  phong. Defaults to '0.9' (optional)</li>
<li><strong>bool refract: Whether the defined envMap should refract. Requires shader</strong>:  phong. Defaults to 'False' (optional)</li>
<li><strong>float refractionRatio: 1/refractive index of the material. Requires shader</strong>:  phong. Defaults to '0.98' (optional)</li>
<li><strong>dict repeat: How many times a texture (defined by src) repeats in the X and Y direction. Defaults to '{'x': 1, 'y'</strong>:  1}' (optional)</li>
<li><strong>float roughness: How rough the material is from 0 to 1. A rougher material will scatter reflected light in more directions than a smooth material. Requires shader</strong>:  standard. Defaults to '0' (optional)</li>
<li><strong>str shader</strong>:  Which material to use. Defaults to the standard material. Can be set to the flat material or to a registered custom shader material. Allows [flat, standard, phong] Defaults to 'standard' (optional)</li>
<li><strong>float shininess: How shiny the specular highlight is; a higher value gives a sharper highlight. Requires shader</strong>:  phong. Defaults to '30' (optional)</li>
<li><strong>str side</strong>:  Which sides of the mesh to render. Allows [front, back, double] Defaults to 'front' (optional)</li>
<li><strong>str specular: This defines how shiny the material is and the color of its shine. Requires shader</strong>:  phong. Defaults to '#111111' (optional)</li>
<li><strong>str src</strong>:  URI, relative or full path of an image/video file. e.g. 'store/users/wiselab/images/360falls.mp4'. (optional)</li>
<li><strong>bool toneMapped: Whether to ignore toneMapping, set to false you are using renderer.toneMapping and an element should appear to emit light. Requires shader</strong>:  flat. Defaults to 'True' (optional)</li>
<li><strong>bool transparent</strong>:  Whether material is transparent. Transparent entities are rendered after non-transparent entities. Defaults to 'False' (optional)</li>
<li><strong>bool vertexColorsEnabled</strong>:  Whether to use vertex or face colors to shade the material. Defaults to 'False' (optional)</li>
<li><strong>bool visible</strong>:  Whether material is visible. Raycasters will ignore invisible materials. Defaults to 'True' (optional)</li>
<li><strong>int width: Width of video (in pixels), if defining a video texture. Requires shader</strong>:  standard or flat. Defaults to '512' (optional)</li>
<li><strong>bool wireframe</strong>:  Whether to render just the geometry edges. Defaults to 'False' (optional)</li>
<li><strong>int wireframeLinewidth</strong>:  Width in px of the rendered line. Defaults to '2' (optional)</li>
</ul>
</div>


                            <div id="Material.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">Material</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#Material.__init__"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="../base_object.html#BaseObject">arena.base_object.BaseObject</a></dt>
                                <dd id="Material.add" class="function"><a href="../base_object.html#BaseObject.add">add</a></dd>
                <dd id="Material.json_encode" class="function"><a href="../base_object.html#BaseObject.json_encode">json_encode</a></dd>
                <dd id="Material.json" class="function"><a href="../base_object.html#BaseObject.json">json</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>

<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:.75rem center;margin-bottom:1rem;}.pdoc .alert > em{display:none;}.pdoc .alert > *:last-child{margin-bottom:0;}.pdoc .alert.note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .alert.warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .alert.danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>