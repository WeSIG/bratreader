from collections import OrderedDict, defaultdict

class Event(object):
    """This class represents an event."""

    def __init__(self, id, mention, trigger, trigger_spans, trigger_label, args, args_spans, args_labels):
        """
        Create an event object.

        :param id: (string) The id of the current annotation.
        :param mention: (string) The string representation of the
        event. Doesn't take into account the fact that event may be
        discontinous.
        :param trigger_spans: (list of list of ints) A list of list of ints
        representing the starting and ending points, in characters, for any
        words in the annotation.
        :param trigger_label: trigger label.
        :param args_spans: (list of list of ints) A list of list of ints
        representing the starting and ending points, in characters, for any
        words in the annotation.
        :param args_labels: trigger label.
        :return: None
        """
        self.id = id
        self.mention = mention
        self.trigger = trigger
        self.trigger_spans = trigger_spans
        self.trigger_label = trigger_label
        self.args = args
        self.args_spans = args_spans
        self.args_labels = args_labels

    def __repr__(self):        
        """Representation of the Annotation."""
        temp_ann = 'Event:' 
        temp_ann = temp_ann + 'id:' + str(self.id)
        temp_ann = temp_ann + '\ttrigger:' + self.trigger
        temp_ann = temp_ann + '\ttrigger_spans:' + str(list(self.trigger_spans))
        temp_ann = temp_ann + '\ttrigger_label:' + str(self.trigger_label)
        temp_ann = temp_ann + '\targs:' + str(self.args)
        temp_ann = temp_ann + '\targs_spans:' + str(list(self.args_spans))
        temp_ann = temp_ann + '\targs_labels:' + str(self.args_labels)
        temp_ann = temp_ann + '\nmention:' + str(self.mention.strip())
        return "{0}".format(temp_ann)
    

    def event2dict(self):        
#         {"arguments": [
#             {"argument_start_index": 2, 
#              "role": "时间", 
#              "argument": "今早", 
#              "alias": []
#              }, 
#             {"argument_start_index": 6, 
#              "role": "震级", 
#              "argument": "2.9级", 
#              "alias": []
#              }
#             ], 
#         "trigger": "地震", 
#         "trigger_start_index": 10, 
#         "class": "灾害/意外", 
#         "event_type": "灾害/意外-地震"
#         }
        
        """Representation of the Annotation."""
        event_dict = {}
        event_dict['trigger'] = self.trigger
        event_dict['trigger_start_index'] = self.trigger_spans[0]
        event_dict['class'] = self.trigger_label
        event_dict['event_type'] = self.trigger_label
        event_dict['arguments'] = []
        for idx_arg in range(len(self.args)):
            arg = {}
            arg['argument'] = self.args[idx_arg]
            arg['argument_start_index'] = self.args_spans[idx_arg][0]
            arg['role'] = self.args_labels[idx_arg]
            arg['alias'] = []
            event_dict['arguments'].append(arg)
        return event_dict
    
