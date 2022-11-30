// Copyright (c) 2022, Palak Padalia and contributors
// For license information, please see license.txt

frappe.ui.form.on('Agent', {
	after_save: function(frm) {
		var agent_name=frm.doc.agent_name
		var follow_me_number=frm.doc.follow_me_number
		alert(agent_name)
		frappe.call({
			method:"important.call_integration.doctype.agent.agent.new_agent",
			
			args:{'agent_name':agent_name,'follow_me_number':follow_me_number},
			callback:function(r){
				alert("done")
			}
		})

		frappe.call({
			method:"important.call_integration.doctype.agent.agent.update_agent",
			
			args:{'agent_name':agent_name,'follow_me_number':follow_me_number},
			callback:function(r){
				alert("updated")
			}
		})
	}
});
