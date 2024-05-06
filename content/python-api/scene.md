---
title: arena.scene
parent: Python API
has_children: true
---
<small>arena-py API <a href="https://github.com/arenaxr/arena-py/blob/v0.10.0/arena">v0.10.0</a></small>
<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
<a href="./../arena.html">arena</a><wbr>.scene    </h1>

                
                
                
                
            </section>
                <section id="Scene">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Scene</span><wbr>(<span class="base"><a href="arena_mqtt.html#ArenaMQTT">arena.arena_mqtt.ArenaMQTT</a></span>):

        
    </div>
    <a class="headerlink" href="#Scene"></a>
    
            <div class="docstring"><p>Gives access to an ARENA scene.
Can create and execute various user-defined functions/tasks.</p>

<h6 id="parameters">Parameters</h6>

<ul>
<li><strong>str host</strong>:  Hostname of the ARENA webserver (required).</li>
<li><strong>str realm</strong>:  Reserved topic fork for future use (optional).</li>
<li><strong>str namespace</strong>:  Username of authenticated user or other namespace (automatic).</li>
<li><strong>str scene</strong>:  The name of the scene, without namespace (required).</li>
</ul>
</div>


                            <div id="Scene.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">Scene</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">host</span><span class="o">=</span><span class="s1">&#39;arenaxr.org&#39;</span>,</span><span class="param">	<span class="n">realm</span><span class="o">=</span><span class="s1">&#39;realm&#39;</span>,</span><span class="param">	<span class="n">network_latency_interval</span><span class="o">=</span><span class="mi">10000</span>,</span><span class="param">	<span class="n">on_msg_callback</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">new_obj_callback</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">user_join_callback</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">user_left_callback</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">delete_obj_callback</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">end_program_callback</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">video</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="n">debug</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="n">cli_args</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#Scene.__init__"></a>
    
    

                            </div>
                            <div id="Scene.telemetry" class="classattr">
                                <div class="attr variable">
            <span class="name">telemetry</span>

        
    </div>
    <a class="headerlink" href="#Scene.telemetry"></a>
    
    

                            </div>
                            <div id="Scene.connected_evt" class="classattr">
                                <div class="attr variable">
            <span class="name">connected_evt</span>

        
    </div>
    <a class="headerlink" href="#Scene.connected_evt"></a>
    
    

                            </div>
                            <div id="Scene.cmd_interpreter" class="classattr">
                                <div class="attr variable">
            <span class="name">cmd_interpreter</span>

        
    </div>
    <a class="headerlink" href="#Scene.cmd_interpreter"></a>
    
    

                            </div>
                            <div id="Scene.parse_cli" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">parse_cli</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">cli_args</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.parse_cli"></a>
    
            <div class="docstring"><p>Reusable command-line options to give apps flexible options to avoid hard-coding locations.</p>
</div>


                            </div>
                            <div id="Scene.exit" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">exit</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">arg</span><span class="o">=</span><span class="mi">0</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.exit"></a>
    
            <div class="docstring"><p>Custom exit to push errors to telemetry</p>
</div>


                            </div>
                            <div id="Scene.on_connect" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_connect</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">client</span>, </span><span class="param"><span class="n">userdata</span>, </span><span class="param"><span class="n">flags</span>, </span><span class="param"><span class="n">rc</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.on_connect"></a>
    
            <div class="docstring"><p>Paho MQTT client on_connect callback</p>
</div>


                            </div>
                            <div id="Scene.on_message" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">client</span>, </span><span class="param"><span class="n">userdata</span>, </span><span class="param"><span class="n">msg</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.on_message"></a>
    
    

                            </div>
                            <div id="Scene.on_publish" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_publish</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">client</span>, </span><span class="param"><span class="n">userdata</span>, </span><span class="param"><span class="n">mid</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.on_publish"></a>
    
    

                            </div>
                            <div id="Scene.process_message" class="classattr">
                                <div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">process_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.process_message"></a>
    
    

                            </div>
                            <div id="Scene.callback_wrapper" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callback_wrapper</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">func</span>, </span><span class="param"><span class="n">arg</span>, </span><span class="param"><span class="n">msg</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.callback_wrapper"></a>
    
            <div class="docstring"><p>Checks for number of arguments for callback</p>
</div>


                            </div>
                            <div id="Scene.generate_custom_event" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">generate_custom_event</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">evt</span>, </span><span class="param"><span class="n">action</span><span class="o">=</span><span class="s1">&#39;clientEvent&#39;</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.generate_custom_event"></a>
    
            <div class="docstring"><p>Publishes an custom event. Could be user or library defined</p>
</div>


                            </div>
                            <div id="Scene.generate_click_event" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">generate_click_event</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span>, </span><span class="param"><span class="nb">type</span><span class="o">=</span><span class="s1">&#39;mousedown&#39;</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.generate_click_event"></a>
    
            <div class="docstring"><p>Publishes an click event</p>
</div>


                            </div>
                            <div id="Scene.manipulate_camera" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">manipulate_camera</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">cam</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.manipulate_camera"></a>
    
            <div class="docstring"><p>Publishes a camera manipulation event</p>
</div>


                            </div>
                            <div id="Scene.look_at" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">look_at</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">cam</span>, </span><span class="param"><span class="n">target</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.look_at"></a>
    
            <div class="docstring"><p>Publishes a camera manipulation event</p>
</div>


                            </div>
                            <div id="Scene.teleport_to_landmark" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">teleport_to_landmark</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">cam</span>, </span><span class="param"><span class="n">target</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.teleport_to_landmark"></a>
    
            <div class="docstring"><p>Publishes a camera manipulation event</p>
</div>


                            </div>
                            <div id="Scene.all_objects" class="classattr">
                                <div class="attr variable">
            <span class="name">all_objects</span>

        
    </div>
    <a class="headerlink" href="#Scene.all_objects"></a>
    
            <div class="docstring"><p>Returns all the objects in a scene</p>
</div>


                            </div>
                            <div id="Scene.add_object" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_object</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.add_object"></a>
    
            <div class="docstring"><p>Public function to create an object</p>
</div>


                            </div>
                            <div id="Scene.add_objects" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_objects</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">objs</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.add_objects"></a>
    
            <div class="docstring"><p>Public function to create multiple objects in a list</p>
</div>


                            </div>
                            <div id="Scene.update_object" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">update_object</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.update_object"></a>
    
            <div class="docstring"><p>Public function to update an object</p>
</div>


                            </div>
                            <div id="Scene.update_objects" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">update_objects</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">objs</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.update_objects"></a>
    
            <div class="docstring"><p>Public function to update multiple objects in a list</p>
</div>


                            </div>
                            <div id="Scene.delete_object" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">delete_object</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.delete_object"></a>
    
            <div class="docstring"><p>Public function to delete an object</p>
</div>


                            </div>
                            <div id="Scene.delete_attributes" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">delete_attributes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span>, </span><span class="param"><span class="n">attributes</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.delete_attributes"></a>
    
            <div class="docstring"><p>Public function to delete a list of 'attributes' as a string[], updating each to null</p>
</div>


                            </div>
                            <div id="Scene.run_animations" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run_animations</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.run_animations"></a>
    
            <div class="docstring"><p>Runs all dispatched animations</p>
</div>


                            </div>
                            <div id="Scene.create_delayed_task" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">create_delayed_task</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span>, </span><span class="param"><span class="n">anim</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.create_delayed_task"></a>
    
            <div class="docstring"><p>Creates a delayed task to push the end state of an animation after the expected
duration. Uses async sleep to avoid blocking.</p>

<h6 id="parameters">Parameters</h6>

<ul>
<li><strong>obj</strong>:  arena object to update</li>
<li><strong>anim</strong>:  Animation to run</li>
</ul>

<h6 id="returns">Returns</h6>

<blockquote>
  <p>created async task</p>
</blockquote>
</div>


                            </div>
                            <div id="Scene.get_persisted_obj" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_persisted_obj</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">object_id</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.get_persisted_obj"></a>
    
            <div class="docstring"><p>Returns a dictionary for a persisted object.</p>

<p>If object is known by arena-py, return local object, not persisted</p>
</div>


                            </div>
                            <div id="Scene.get_persisted_objs" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_persisted_objs</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.get_persisted_objs"></a>
    
            <div class="docstring"><p>Returns a dictionary of persisted objects.</p>

<p>If object is known by arena-py, return our local object, not persisted
Silently fails/skip objects without object_id and object_type (except programs)
Instantiates generic Object if object_type is given but unknown to arena-py</p>
</div>


                            </div>
                            <div id="Scene.get_persisted_scene_option" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_persisted_scene_option</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.get_persisted_scene_option"></a>
    
            <div class="docstring"><p>Returns a dictionary for scene-options. [TODO] wrap the output as a BaseObject</p>
</div>


                            </div>
                            <div id="Scene.get_writable_scenes" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_writable_scenes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.get_writable_scenes"></a>
    
            <div class="docstring"><p>Request list of scene names for logged in user account that user has publish permission for.
Returns: list of scenes.</p>
</div>


                            </div>
                            <div id="Scene.get_user_list" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_user_list</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.get_user_list"></a>
    
            <div class="docstring"><p>Returns a list of users</p>
</div>


                            </div>
                            <div id="Scene.get_rcv_pub_queue_len" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_rcv_pub_queue_len</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.get_rcv_pub_queue_len"></a>
    
            <div class="docstring"><p>Return QueueStats object with receive and publish queue length</p>
</div>


                            </div>
                            <div id="Scene.run_info_update" class="classattr">
                                <div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run_info_update</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">run_info</span></span><span class="return-annotation">):</span></span>

        
    </div>
    <a class="headerlink" href="#Scene.run_info_update"></a>
    
            <div class="docstring"><p>Callback when program stats are updated; publish program object update</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="arena_mqtt.html#ArenaMQTT">arena.arena_mqtt.ArenaMQTT</a></dt>
                                <dd id="Scene.scene" class="variable"><a href="arena_mqtt.html#ArenaMQTT.scene">scene</a></dd>
                <dd id="Scene.device" class="variable"><a href="arena_mqtt.html#ArenaMQTT.device">device</a></dd>
                <dd id="Scene.auth" class="variable"><a href="arena_mqtt.html#ArenaMQTT.auth">auth</a></dd>
                <dd id="Scene.debug" class="variable"><a href="arena_mqtt.html#ArenaMQTT.debug">debug</a></dd>
                <dd id="Scene.username" class="variable"><a href="arena_mqtt.html#ArenaMQTT.username">username</a></dd>
                <dd id="Scene.remote_auth_token" class="variable"><a href="arena_mqtt.html#ArenaMQTT.remote_auth_token">remote_auth_token</a></dd>
                <dd id="Scene.mqttc_id" class="variable"><a href="arena_mqtt.html#ArenaMQTT.mqttc_id">mqttc_id</a></dd>
                <dd id="Scene.config_url" class="variable"><a href="arena_mqtt.html#ArenaMQTT.config_url">config_url</a></dd>
                <dd id="Scene.config_data" class="variable"><a href="arena_mqtt.html#ArenaMQTT.config_data">config_data</a></dd>
                <dd id="Scene.mqtt_host" class="variable"><a href="arena_mqtt.html#ArenaMQTT.mqtt_host">mqtt_host</a></dd>
                <dd id="Scene.subscribe_topic" class="variable"><a href="arena_mqtt.html#ArenaMQTT.subscribe_topic">subscribe_topic</a></dd>
                <dd id="Scene.latency_topic" class="variable"><a href="arena_mqtt.html#ArenaMQTT.latency_topic">latency_topic</a></dd>
                <dd id="Scene.ignore_topic" class="variable"><a href="arena_mqtt.html#ArenaMQTT.ignore_topic">ignore_topic</a></dd>
                <dd id="Scene.mqttc" class="variable"><a href="arena_mqtt.html#ArenaMQTT.mqttc">mqttc</a></dd>
                <dd id="Scene.can_publish" class="variable"><a href="arena_mqtt.html#ArenaMQTT.can_publish">can_publish</a></dd>
                <dd id="Scene.on_msg_callback" class="variable"><a href="arena_mqtt.html#ArenaMQTT.on_msg_callback">on_msg_callback</a></dd>
                <dd id="Scene.end_program_callback" class="variable"><a href="arena_mqtt.html#ArenaMQTT.end_program_callback">end_program_callback</a></dd>
                <dd id="Scene.event_loop" class="variable"><a href="arena_mqtt.html#ArenaMQTT.event_loop">event_loop</a></dd>
                <dd id="Scene.mqtt_connect_evt" class="variable"><a href="arena_mqtt.html#ArenaMQTT.mqtt_connect_evt">mqtt_connect_evt</a></dd>
                <dd id="Scene.msg_queue" class="variable"><a href="arena_mqtt.html#ArenaMQTT.msg_queue">msg_queue</a></dd>
                <dd id="Scene.generate_client_id" class="function"><a href="arena_mqtt.html#ArenaMQTT.generate_client_id">generate_client_id</a></dd>
                <dd id="Scene.network_latency_update" class="function"><a href="arena_mqtt.html#ArenaMQTT.network_latency_update">network_latency_update</a></dd>
                <dd id="Scene.run_once" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_once">run_once</a></dd>
                <dd id="Scene.run_after_interval" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_after_interval">run_after_interval</a></dd>
                <dd id="Scene.run_async" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_async">run_async</a></dd>
                <dd id="Scene.run_forever" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_forever">run_forever</a></dd>
                <dd id="Scene.run_tasks" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_tasks">run_tasks</a></dd>
                <dd id="Scene.stop_tasks" class="function"><a href="arena_mqtt.html#ArenaMQTT.stop_tasks">stop_tasks</a></dd>
                <dd id="Scene.sleep" class="function"><a href="arena_mqtt.html#ArenaMQTT.sleep">sleep</a></dd>
                <dd id="Scene.on_disconnect" class="function"><a href="arena_mqtt.html#ArenaMQTT.on_disconnect">on_disconnect</a></dd>
                <dd id="Scene.disconnect" class="function"><a href="arena_mqtt.html#ArenaMQTT.disconnect">disconnect</a></dd>
                <dd id="Scene.message_callback_add" class="function"><a href="arena_mqtt.html#ArenaMQTT.message_callback_add">message_callback_add</a></dd>
                <dd id="Scene.message_callback_remove" class="function"><a href="arena_mqtt.html#ArenaMQTT.message_callback_remove">message_callback_remove</a></dd>
                <dd id="Scene.rcv_queue_len" class="function"><a href="arena_mqtt.html#ArenaMQTT.rcv_queue_len">rcv_queue_len</a></dd>
                <dd id="Scene.pub_queue_len" class="function"><a href="arena_mqtt.html#ArenaMQTT.pub_queue_len">pub_queue_len</a></dd>
                <dd id="Scene.client_id" class="function"><a href="arena_mqtt.html#ArenaMQTT.client_id">client_id</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Arena">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Arena</span><wbr>(<span class="base"><a href="#Scene">Scene</a></span>):

        
    </div>
    <a class="headerlink" href="#Arena"></a>
    
            <div class="docstring"><p>Another name for Scene.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#Scene">Scene</a></dt>
                                <dd id="Arena.__init__" class="function"><a href="#Scene.__init__">Scene</a></dd>
                <dd id="Arena.telemetry" class="variable"><a href="#Scene.telemetry">telemetry</a></dd>
                <dd id="Arena.connected_evt" class="variable"><a href="#Scene.connected_evt">connected_evt</a></dd>
                <dd id="Arena.cmd_interpreter" class="variable"><a href="#Scene.cmd_interpreter">cmd_interpreter</a></dd>
                <dd id="Arena.parse_cli" class="function"><a href="#Scene.parse_cli">parse_cli</a></dd>
                <dd id="Arena.exit" class="function"><a href="#Scene.exit">exit</a></dd>
                <dd id="Arena.on_connect" class="function"><a href="#Scene.on_connect">on_connect</a></dd>
                <dd id="Arena.on_message" class="function"><a href="#Scene.on_message">on_message</a></dd>
                <dd id="Arena.on_publish" class="function"><a href="#Scene.on_publish">on_publish</a></dd>
                <dd id="Arena.process_message" class="function"><a href="#Scene.process_message">process_message</a></dd>
                <dd id="Arena.callback_wrapper" class="function"><a href="#Scene.callback_wrapper">callback_wrapper</a></dd>
                <dd id="Arena.generate_custom_event" class="function"><a href="#Scene.generate_custom_event">generate_custom_event</a></dd>
                <dd id="Arena.generate_click_event" class="function"><a href="#Scene.generate_click_event">generate_click_event</a></dd>
                <dd id="Arena.manipulate_camera" class="function"><a href="#Scene.manipulate_camera">manipulate_camera</a></dd>
                <dd id="Arena.look_at" class="function"><a href="#Scene.look_at">look_at</a></dd>
                <dd id="Arena.teleport_to_landmark" class="function"><a href="#Scene.teleport_to_landmark">teleport_to_landmark</a></dd>
                <dd id="Arena.all_objects" class="variable"><a href="#Scene.all_objects">all_objects</a></dd>
                <dd id="Arena.add_object" class="function"><a href="#Scene.add_object">add_object</a></dd>
                <dd id="Arena.add_objects" class="function"><a href="#Scene.add_objects">add_objects</a></dd>
                <dd id="Arena.update_object" class="function"><a href="#Scene.update_object">update_object</a></dd>
                <dd id="Arena.update_objects" class="function"><a href="#Scene.update_objects">update_objects</a></dd>
                <dd id="Arena.delete_object" class="function"><a href="#Scene.delete_object">delete_object</a></dd>
                <dd id="Arena.delete_attributes" class="function"><a href="#Scene.delete_attributes">delete_attributes</a></dd>
                <dd id="Arena.run_animations" class="function"><a href="#Scene.run_animations">run_animations</a></dd>
                <dd id="Arena.create_delayed_task" class="function"><a href="#Scene.create_delayed_task">create_delayed_task</a></dd>
                <dd id="Arena.get_persisted_obj" class="function"><a href="#Scene.get_persisted_obj">get_persisted_obj</a></dd>
                <dd id="Arena.get_persisted_objs" class="function"><a href="#Scene.get_persisted_objs">get_persisted_objs</a></dd>
                <dd id="Arena.get_persisted_scene_option" class="function"><a href="#Scene.get_persisted_scene_option">get_persisted_scene_option</a></dd>
                <dd id="Arena.get_writable_scenes" class="function"><a href="#Scene.get_writable_scenes">get_writable_scenes</a></dd>
                <dd id="Arena.get_user_list" class="function"><a href="#Scene.get_user_list">get_user_list</a></dd>
                <dd id="Arena.get_rcv_pub_queue_len" class="function"><a href="#Scene.get_rcv_pub_queue_len">get_rcv_pub_queue_len</a></dd>
                <dd id="Arena.run_info_update" class="function"><a href="#Scene.run_info_update">run_info_update</a></dd>

            </div>
            <div><dt><a href="arena_mqtt.html#ArenaMQTT">arena.arena_mqtt.ArenaMQTT</a></dt>
                                <dd id="Arena.scene" class="variable"><a href="arena_mqtt.html#ArenaMQTT.scene">scene</a></dd>
                <dd id="Arena.device" class="variable"><a href="arena_mqtt.html#ArenaMQTT.device">device</a></dd>
                <dd id="Arena.auth" class="variable"><a href="arena_mqtt.html#ArenaMQTT.auth">auth</a></dd>
                <dd id="Arena.debug" class="variable"><a href="arena_mqtt.html#ArenaMQTT.debug">debug</a></dd>
                <dd id="Arena.username" class="variable"><a href="arena_mqtt.html#ArenaMQTT.username">username</a></dd>
                <dd id="Arena.remote_auth_token" class="variable"><a href="arena_mqtt.html#ArenaMQTT.remote_auth_token">remote_auth_token</a></dd>
                <dd id="Arena.mqttc_id" class="variable"><a href="arena_mqtt.html#ArenaMQTT.mqttc_id">mqttc_id</a></dd>
                <dd id="Arena.config_url" class="variable"><a href="arena_mqtt.html#ArenaMQTT.config_url">config_url</a></dd>
                <dd id="Arena.config_data" class="variable"><a href="arena_mqtt.html#ArenaMQTT.config_data">config_data</a></dd>
                <dd id="Arena.mqtt_host" class="variable"><a href="arena_mqtt.html#ArenaMQTT.mqtt_host">mqtt_host</a></dd>
                <dd id="Arena.subscribe_topic" class="variable"><a href="arena_mqtt.html#ArenaMQTT.subscribe_topic">subscribe_topic</a></dd>
                <dd id="Arena.latency_topic" class="variable"><a href="arena_mqtt.html#ArenaMQTT.latency_topic">latency_topic</a></dd>
                <dd id="Arena.ignore_topic" class="variable"><a href="arena_mqtt.html#ArenaMQTT.ignore_topic">ignore_topic</a></dd>
                <dd id="Arena.mqttc" class="variable"><a href="arena_mqtt.html#ArenaMQTT.mqttc">mqttc</a></dd>
                <dd id="Arena.can_publish" class="variable"><a href="arena_mqtt.html#ArenaMQTT.can_publish">can_publish</a></dd>
                <dd id="Arena.on_msg_callback" class="variable"><a href="arena_mqtt.html#ArenaMQTT.on_msg_callback">on_msg_callback</a></dd>
                <dd id="Arena.end_program_callback" class="variable"><a href="arena_mqtt.html#ArenaMQTT.end_program_callback">end_program_callback</a></dd>
                <dd id="Arena.event_loop" class="variable"><a href="arena_mqtt.html#ArenaMQTT.event_loop">event_loop</a></dd>
                <dd id="Arena.mqtt_connect_evt" class="variable"><a href="arena_mqtt.html#ArenaMQTT.mqtt_connect_evt">mqtt_connect_evt</a></dd>
                <dd id="Arena.msg_queue" class="variable"><a href="arena_mqtt.html#ArenaMQTT.msg_queue">msg_queue</a></dd>
                <dd id="Arena.generate_client_id" class="function"><a href="arena_mqtt.html#ArenaMQTT.generate_client_id">generate_client_id</a></dd>
                <dd id="Arena.network_latency_update" class="function"><a href="arena_mqtt.html#ArenaMQTT.network_latency_update">network_latency_update</a></dd>
                <dd id="Arena.run_once" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_once">run_once</a></dd>
                <dd id="Arena.run_after_interval" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_after_interval">run_after_interval</a></dd>
                <dd id="Arena.run_async" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_async">run_async</a></dd>
                <dd id="Arena.run_forever" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_forever">run_forever</a></dd>
                <dd id="Arena.run_tasks" class="function"><a href="arena_mqtt.html#ArenaMQTT.run_tasks">run_tasks</a></dd>
                <dd id="Arena.stop_tasks" class="function"><a href="arena_mqtt.html#ArenaMQTT.stop_tasks">stop_tasks</a></dd>
                <dd id="Arena.sleep" class="function"><a href="arena_mqtt.html#ArenaMQTT.sleep">sleep</a></dd>
                <dd id="Arena.on_disconnect" class="function"><a href="arena_mqtt.html#ArenaMQTT.on_disconnect">on_disconnect</a></dd>
                <dd id="Arena.disconnect" class="function"><a href="arena_mqtt.html#ArenaMQTT.disconnect">disconnect</a></dd>
                <dd id="Arena.message_callback_add" class="function"><a href="arena_mqtt.html#ArenaMQTT.message_callback_add">message_callback_add</a></dd>
                <dd id="Arena.message_callback_remove" class="function"><a href="arena_mqtt.html#ArenaMQTT.message_callback_remove">message_callback_remove</a></dd>
                <dd id="Arena.rcv_queue_len" class="function"><a href="arena_mqtt.html#ArenaMQTT.rcv_queue_len">rcv_queue_len</a></dd>
                <dd id="Arena.pub_queue_len" class="function"><a href="arena_mqtt.html#ArenaMQTT.pub_queue_len">pub_queue_len</a></dd>
                <dd id="Arena.client_id" class="function"><a href="arena_mqtt.html#ArenaMQTT.client_id">client_id</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>

<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>