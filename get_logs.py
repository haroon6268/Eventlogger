import win32evtlog

#LOG TYPES: SYSTEM, APPLICATION, SECURITY, SETUP, FORWARDED EVENTS
def get_logs(log_type):
    log_handle = win32evtlog.OpenEventLog('localhost', log_type)

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    events = win32evtlog.ReadEventLog(log_handle, flags, 0)

    output = []
    for event in events:
        cur = {}
        cur["event_catagory"] = event.EventCategory
        cur["time_generated"]= event.TimeGenerated
        cur["source_name"]=event.SourceName
        cur["event_id"]= event.EventID
        cur["event_type"]= event.EventType
        cur["event_string"] = event.StringInserts
        print(cur)
        output.append(cur)
    win32evtlog.CloseEventLog(log_handle)
    return output

#Application Logs, Setup, System, Security

