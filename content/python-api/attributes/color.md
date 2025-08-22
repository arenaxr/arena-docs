---
title: arena.attributes.color
parent: arena.attributes
grand_parent: Python API
---

<!-- This file is auto-generated from github.com/arena-docs/scripts/pdoc, changes here may be overwritten. -->

<small>arena-py API <a href="https://github.com/arenaxr/arena-py/blob/v1.4.0/arena">v1.4.0</a></small>
<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
<a href="./../arena.html">arena</a><wbr>.<a href="./../attributes.html">attributes</a><wbr>.color    </h1>

                
                
                
                
            </section>
                <section id="Color">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Color</span><wbr>(<span class="base"><a href="attribute.html#Attribute">arena.attributes.attribute.Attribute</a></span>):

        
    </div>
    <a class="headerlink" href="#Color"></a>
    
            <div class="docstring"><p>Color Attribute.
Usage: <code>color=Color(red,green,blue)</code> or <code>color=(red,green,blue)</code></p>
</div>


                            <div id="Color.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">Color</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">red</span><span class="o">=</span><span class="mi">0</span>, </span><span class="param"><span class="n">green</span><span class="o">=</span><span class="mi">0</span>, </span><span class="param"><span class="n">blue</span><span class="o">=</span><span class="mi">0</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#Color.__init__"></a>
    
    

                            </div>
                            <div id="Color.hex" class="classattr">
                                <div class="attr variable">
            <span class="name">hex</span>

        
    </div>
    <a class="headerlink" href="#Color.hex"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="../base_object.html#BaseObject">arena.base_object.BaseObject</a></dt>
                                <dd id="Color.add" class="function"><a href="../base_object.html#BaseObject.add">add</a></dd>
                <dd id="Color.json_encode" class="function"><a href="../base_object.html#BaseObject.json_encode">json_encode</a></dd>
                <dd id="Color.json" class="function"><a href="../base_object.html#BaseObject.json">json</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="COLOR_NAMES">
                    <div class="attr variable">
            <span class="name">COLOR_NAMES</span>        =
<input id="COLOR_NAMES-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="COLOR_NAMES-view-value"></label><span class="default_value">{&#39;aliceblue&#39;: (240, 248, 255), &#39;antiquewhite&#39;: (250, 235, 215), &#39;aqua&#39;: (0, 255, 255), &#39;aquamarine&#39;: (127, 255, 212), &#39;azure&#39;: (240, 255, 255), &#39;beige&#39;: (245, 245, 220), &#39;bisque&#39;: (255, 228, 196), &#39;black&#39;: (0, 0, 0), &#39;blanchedalmond&#39;: (255, 235, 205), &#39;blue&#39;: (0, 0, 255), &#39;blueviolet&#39;: (138, 43, 226), &#39;brown&#39;: (165, 42, 42), &#39;burlywood&#39;: (222, 184, 135), &#39;cadetblue&#39;: (95, 158, 160), &#39;chartreuse&#39;: (127, 255, 0), &#39;chocolate&#39;: (210, 105, 30), &#39;coral&#39;: (255, 127, 80), &#39;cornflowerblue&#39;: (100, 149, 237), &#39;cornsilk&#39;: (255, 248, 220), &#39;crimson&#39;: (220, 20, 60), &#39;cyan&#39;: (0, 255, 255), &#39;darkblue&#39;: (0, 0, 139), &#39;darkcyan&#39;: (0, 139, 139), &#39;darkgoldenrod&#39;: (184, 134, 11), &#39;darkgray&#39;: (169, 169, 169), &#39;darkgreen&#39;: (0, 100, 0), &#39;darkkhaki&#39;: (189, 183, 107), &#39;darkmagenta&#39;: (139, 0, 139), &#39;darkolivegreen&#39;: (85, 107, 47), &#39;darkorange&#39;: (255, 140, 0), &#39;darkorchid&#39;: (153, 50, 204), &#39;darkred&#39;: (139, 0, 0), &#39;darksalmon&#39;: (233, 150, 122), &#39;darkseagreen&#39;: (143, 188, 143), &#39;darkslateblue&#39;: (72, 61, 139), &#39;darkslategray&#39;: (47, 79, 79), &#39;darkturquoise&#39;: (0, 206, 209), &#39;darkviolet&#39;: (148, 0, 211), &#39;deeppink&#39;: (255, 20, 147), &#39;deepskyblue&#39;: (0, 191, 255), &#39;dimgray&#39;: (105, 105, 105), &#39;dodgerblue&#39;: (30, 144, 255), &#39;firebrick&#39;: (178, 34, 34), &#39;floralwhite&#39;: (255, 250, 240), &#39;forestgreen&#39;: (34, 139, 34), &#39;fuchsia&#39;: (255, 0, 255), &#39;gainsboro&#39;: (220, 220, 220), &#39;ghostwhite&#39;: (248, 248, 255), &#39;gold&#39;: (255, 215, 0), &#39;goldenrod&#39;: (218, 165, 32), &#39;gray&#39;: (128, 128, 128), &#39;green&#39;: (0, 128, 0), &#39;greenyellow&#39;: (173, 255, 47), &#39;honeydew&#39;: (240, 255, 240), &#39;hotpink&#39;: (255, 105, 180), &#39;indianred&#39;: (205, 92, 92), &#39;indigo&#39;: (75, 0, 130), &#39;ivory&#39;: (255, 255, 240), &#39;khaki&#39;: (240, 230, 140), &#39;lavender&#39;: (230, 230, 250), &#39;lavenderblush&#39;: (255, 240, 245), &#39;lawngreen&#39;: (124, 252, 0), &#39;lemonchiffon&#39;: (255, 250, 205), &#39;lightblue&#39;: (173, 216, 230), &#39;lightcoral&#39;: (240, 128, 128), &#39;lightcyan&#39;: (224, 255, 255), &#39;lightgoldenrodyellow&#39;: (250, 250, 210), &#39;lightgray&#39;: (211, 211, 211), &#39;lightgreen&#39;: (144, 238, 144), &#39;lightpink&#39;: (255, 182, 193), &#39;lightsalmon&#39;: (255, 160, 122), &#39;lightseagreen&#39;: (32, 178, 170), &#39;lightskyblue&#39;: (135, 206, 250), &#39;lightslategray&#39;: (119, 136, 153), &#39;lightsteelblue&#39;: (176, 196, 222), &#39;lightyellow&#39;: (255, 255, 224), &#39;lime&#39;: (0, 255, 0), &#39;limegreen&#39;: (50, 205, 50), &#39;linen&#39;: (250, 240, 230), &#39;magenta&#39;: (255, 0, 255), &#39;maroon&#39;: (128, 0, 0), &#39;mediumaquamarine&#39;: (102, 205, 170), &#39;mediumblue&#39;: (0, 0, 205), &#39;mediumorchid&#39;: (186, 85, 211), &#39;mediumpurple&#39;: (147, 112, 219), &#39;mediumseagreen&#39;: (60, 179, 113), &#39;mediumslateblue&#39;: (123, 104, 238), &#39;mediumspringgreen&#39;: (0, 250, 154), &#39;mediumturquoise&#39;: (72, 209, 204), &#39;mediumvioletred&#39;: (199, 21, 133), &#39;midnightblue&#39;: (25, 25, 112), &#39;mintcream&#39;: (245, 255, 250), &#39;mistyrose&#39;: (255, 228, 225), &#39;moccasin&#39;: (255, 228, 181), &#39;navajowhite&#39;: (255, 222, 173), &#39;navy&#39;: (0, 0, 128), &#39;oldlace&#39;: (253, 245, 230), &#39;olive&#39;: (128, 128, 0), &#39;olivedrab&#39;: (107, 142, 35), &#39;orange&#39;: (255, 165, 0), &#39;orangered&#39;: (255, 69, 0), &#39;orchid&#39;: (218, 112, 214), &#39;palegoldenrod&#39;: (238, 232, 170), &#39;palegreen&#39;: (152, 251, 152), &#39;paleturquoise&#39;: (175, 238, 238), &#39;palevioletred&#39;: (219, 112, 147), &#39;papayawhip&#39;: (255, 239, 213), &#39;peachpuff&#39;: (255, 218, 185), &#39;peru&#39;: (205, 133, 63), &#39;pink&#39;: (255, 192, 203), &#39;plum&#39;: (221, 160, 221), &#39;powderblue&#39;: (176, 224, 230), &#39;purple&#39;: (128, 0, 128), &#39;red&#39;: (255, 0, 0), &#39;rosybrown&#39;: (188, 143, 143), &#39;royalblue&#39;: (65, 105, 225), &#39;saddlebrown&#39;: (139, 69, 19), &#39;salmon&#39;: (250, 128, 114), &#39;sandybrown&#39;: (244, 164, 96), &#39;seagreen&#39;: (46, 139, 87), &#39;seashell&#39;: (255, 245, 238), &#39;sienna&#39;: (160, 82, 45), &#39;silver&#39;: (192, 192, 192), &#39;skyblue&#39;: (135, 206, 235), &#39;slateblue&#39;: (106, 90, 205), &#39;slategray&#39;: (112, 128, 144), &#39;snow&#39;: (255, 250, 250), &#39;springgreen&#39;: (0, 255, 127), &#39;steelblue&#39;: (70, 130, 180), &#39;tan&#39;: (210, 180, 140), &#39;teal&#39;: (0, 128, 128), &#39;thistle&#39;: (216, 191, 216), &#39;tomato&#39;: (255, 99, 71), &#39;turquoise&#39;: (64, 224, 208), &#39;violet&#39;: (238, 130, 238), &#39;wheat&#39;: (245, 222, 179), &#39;white&#39;: (255, 255, 255), &#39;whitesmoke&#39;: (245, 245, 245), &#39;yellow&#39;: (255, 255, 0), &#39;yellowgreen&#39;: (154, 205, 50)}</span>

        
    </div>
    <a class="headerlink" href="#COLOR_NAMES"></a>
    
    

                </section>
                <section id="name_to_rgb">
                    <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">name_to_rgb</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">color_name</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#name_to_rgb"></a>
    
            <div class="docstring"><p>Convert color name to RGB tuple.
Returns RGB tuple or None if color not found.</p>
</div>


                </section>
    </main>

<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:.75rem center;margin-bottom:1rem;}.pdoc .alert > em{display:none;}.pdoc .alert > *:last-child{margin-bottom:0;}.pdoc .alert.note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .alert.warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .alert.danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>