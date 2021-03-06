# MythSource for URLs
#     http://zaran:8280/source/xref/mythtv/mythtv/programs/mythbackend/mythxml.cpp
#
# http://squiggy:6544/Myth/GetProgramGuide?StartTime=1985-04-12T10:15:30&EndTime=2011-04-12T10:15:30&NumOfChannels=100
#
# http://squiggy:6544/Myth/GetConnectionInfo
#
#    <?xml version="1.0" encoding="utf-8"?>
#    <GetConnectionInfoResponse>
#        <Info><Database><Host>zaran</Host><Port>0</Port><UserName>mythtv</UserName><Password>XXX</Password><Name>squiggy</Name><Type>QMYSQL3</Type></Database><WOL><Enabled>0</Enabled><Reconnect>0</Reconnect><Retry>0</Retry><Command></Command></WOL></Info>
#    </GetConnectionInfoResponse>
#  
# http://squiggy:6544/Myth/GetServDesc
#
#    <?xml version="1.0" encoding="utf-8"?>
#    <scpd xmlns="urn:schemas-upnp-org:service-1-0">
#       <specVersion>
#          <major>1</major>
#          <minor>0</minor>
#       </specVersion>
#       <actionList>
#          <action>
#             <name>GetAlbumArt</name>
#    
#             <argumentList>
#                <argument>
#                   <name>Id</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Id</relatedStateVariable>
#                </argument>
#                <argument>
#    
#                   <name>Height</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Height</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Width</name>
#                   <direction>in</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_Width</relatedStateVariable>
#                </argument>
#             </argumentList>
#          </action>
#          <action>
#             <name>GetChannelIcon</name>
#             <argumentList>
#                <argument>
#    
#                   <name>ChanId</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_ChanId</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Height</name>
#                   <direction>in</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_Height</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Width</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Width</relatedStateVariable>
#                </argument>
#    
#             </argumentList>
#          </action>
#          <action>
#             <name>GetConnectionInfo</name>
#             <argumentList>
#                <argument>
#                   <name>Pin</name>
#                   <direction>in</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_Value</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Info</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_XML</relatedStateVariable>
#                </argument>
#    
#             </argumentList>
#          </action>
#          <action>
#             <name>GetExpiring</name>
#             <argumentList>
#                <argument>
#                   <name>Count</name>
#                   <direction>out</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_Count</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>AsOf</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Time</relatedStateVariable>
#                </argument>
#    
#                <argument>
#                   <name>Version</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Version</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>ProtoVer</name>
#    
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_ProtoVer</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Expiring</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_XML</relatedStateVariable>
#    
#                </argument>
#             </argumentList>
#          </action>
#          <action>
#             <name>GetHosts</name>
#             <argumentList>
#                <argument>
#                   <name>Count</name>
#    
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Count</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Hosts</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_XML</relatedStateVariable>
#    
#                </argument>
#             </argumentList>
#          </action>
#          <action>
#             <name>GetKeys</name>
#             <argumentList>
#                <argument>
#                   <name>Count</name>
#    
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Count</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Keys</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_XML</relatedStateVariable>
#    
#                </argument>
#             </argumentList>
#          </action>
#          <action>
#             <name>GetMusic</name>
#             <argumentList>
#                <argument>
#                   <name>Id</name>
#    
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Id</relatedStateVariable>
#                </argument>
#             </argumentList>
#          </action>
#          <action>
#             <name>GetPreviewImage</name>
#    
#             <argumentList>
#                <argument>
#                   <name>ChanId</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_ChanId</relatedStateVariable>
#                </argument>
#                <argument>
#    
#                   <name>StartTime</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Time</relatedStateVariable>
#                </argument>
#             </argumentList>
#          </action>
#          <action>
#    
#             <name>GetProgramDetails</name>
#             <argumentList>
#                <argument>
#                   <name>ChanId</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_ChanId</relatedStateVariable>
#                </argument>
#    
#                <argument>
#                   <name>StartTime</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Time</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Count</name>
#    
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Count</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>AsOf</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Time</relatedStateVariable>
#    
#                </argument>
#                <argument>
#                   <name>Version</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Version</relatedStateVariable>
#                </argument>
#                <argument>
#    
#                   <name>ProtoVer</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_ProtoVer</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>ProgramDetails</name>
#                   <direction>out</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_XML</relatedStateVariable>
#                </argument>
#             </argumentList>
#          </action>
#          <action>
#             <name>GetProgramGuide</name>
#             <argumentList>
#                <argument>
#    
#                   <name>StartTime</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Time</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>EndTime</name>
#                   <direction>in</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_Time</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>StartChanId</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_ChanId</relatedStateVariable>
#                </argument>
#    
#                <argument>
#                   <name>NumOfCannels</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Count</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Details</name>
#    
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Bool</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Count</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Count</relatedStateVariable>
#    
#                </argument>
#                <argument>
#                   <name>AsOf</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Time</relatedStateVariable>
#                </argument>
#                <argument>
#    
#                   <name>Version</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Version</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>ProtoVer</name>
#                   <direction>out</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_ProtoVer</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>ProgramGuide</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_XML</relatedStateVariable>
#                </argument>
#    
#             </argumentList>
#          </action>
#          <action>
#             <name>GetRecorded</name>
#             <argumentList>
#                <argument>
#                   <name>Descending</name>
#                   <direction>in</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_Bool</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Count</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Count</relatedStateVariable>
#                </argument>
#    
#                <argument>
#                   <name>AsOf</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Time</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Version</name>
#    
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Version</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>ProtoVer</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_ProtoVer</relatedStateVariable>
#    
#                </argument>
#                <argument>
#                   <name>Recorded</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_XML</relatedStateVariable>
#                </argument>
#             </argumentList>
#    
#          </action>
#          <action>
#             <name>GetRecording</name>
#             <argumentList>
#                <argument>
#                   <name>ChanId</name>
#                   <direction>in</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_ChanId</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>StartTime</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Time</relatedStateVariable>
#                </argument>
#    
#             </argumentList>
#          </action>
#          <action>
#             <name>GetSetting</name>
#             <argumentList>
#                <argument>
#                   <name>Key</name>
#                   <direction>in</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_Key</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>HostName</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_HostName</relatedStateVariable>
#                </argument>
#    
#                <argument>
#                   <name>Default</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Value</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Count</name>
#    
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Count</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Values</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_XML</relatedStateVariable>
#    
#                </argument>
#             </argumentList>
#          </action>
#          <action>
#             <name>GetVideo</name>
#             <argumentList>
#                <argument>
#                   <name>Id</name>
#    
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Id</relatedStateVariable>
#                </argument>
#             </argumentList>
#          </action>
#          <action>
#             <name>PutSetting</name>
#    
#             <argumentList>
#                <argument>
#                   <name>Key</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Key</relatedStateVariable>
#                </argument>
#                <argument>
#    
#                   <name>HostName</name>
#                   <direction>in</direction>
#                   <relatedStateVariable>A_ARG_TYPE_HostName</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Value</name>
#                   <direction>in</direction>
#    
#                   <relatedStateVariable>A_ARG_TYPE_Value</relatedStateVariable>
#                </argument>
#                <argument>
#                   <name>Result</name>
#                   <direction>out</direction>
#                   <relatedStateVariable>A_ARG_TYPE_Bool</relatedStateVariable>
#                </argument>
#    
#             </argumentList>
#          </action>
#       </actionList>
#       <serviceStateTable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_Version</name>
#             <dataType>string</dataType>
#          </stateVariable>
#    
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_Time</name>
#             <dataType>string</dataType>
#          </stateVariable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_ChanId</name>
#             <dataType>string</dataType>
#    
#          </stateVariable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_Value</name>
#             <dataType>string</dataType>
#          </stateVariable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_Key</name>
#    
#             <dataType>string</dataType>
#          </stateVariable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_ProtoVer</name>
#             <dataType>string</dataType>
#          </stateVariable>
#          <stateVariable sendEvents="no">
#    
#             <name>A_ARG_TYPE_Id</name>
#             <dataType>i2</dataType>
#          </stateVariable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_Bool</name>
#             <dataType>boolean</dataType>
#          </stateVariable>
#    
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_XML</name>
#             <dataType>string</dataType>
#          </stateVariable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_Count</name>
#             <dataType>i2</dataType>
#    
#          </stateVariable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_HostName</name>
#             <dataType>string</dataType>
#          </stateVariable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_Height</name>
#    
#             <dataType>i2</dataType>
#          </stateVariable>
#          <stateVariable sendEvents="no">
#             <name>A_ARG_TYPE_Width</name>
#             <dataType>i2</dataType>
#          </stateVariable>
#       </serviceStateTable>
#    
#    </scpd>
