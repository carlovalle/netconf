from ncclient import manager
from lxml import etree
import sys
import xml.dom.minidom

#####################################################################################################
#                                                                                                   #
#               device is a type nclient.manager.Manager that can  manage                           #
#               all the rpc statement as a file                                                     #
#                                                                                                   #
#####################################################################################################

device = manager.connect(host="ios-xe-mgmt.cisco.com", port=10000, username="developer", password="C1sco12345", hostkey_verify=False, 
                         device_params={'name': 'default'}, allow_agent=False, look_for_keys=False)


get_interfaces_ietf="""
<filter>
 <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
  </interface>
 </interfaces>
</filter>
"""
get_interfaces_oc = """
<filter>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name/>
            <config>
                <type>ianaift:softwareLoopback</type>
            </config>
            <subinterfaces/>
        </interface>
    </interfaces>
</filter>
"""

get_bgp = """
  <filter>
    <oc-bgp:bgp xmlns:oc-bgp="http://openconfig.net/yang/bgp"/>
  </filter>
"""


#####################################################################################################
#                                                                                                   #
#               the method get receives the reply of the Router when this                           #
#               sends the <get-config> rpc. You only have to change the parameter                   #
#               in file object.                                                                     #
#                                                                                                   #
#####################################################################################################


with device as m:
  get = (m.get_config('running',filter=get_bgp))
print(xml.dom.minidom.parseString(get.xml).toprettyxml())
