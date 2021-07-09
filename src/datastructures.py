
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [{
            "first_name": "John",
            "last_name": "Jackson",
            "id": 1,
            "children": []
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if "parent" in member:
            for grandparent in self._members:
                if grandparent["first_name"] == member["parent"]:
                    if "children" in grandparent:
                        grandparent["children"].append(member)
                    else:
                        grandparent["children"] = [member]
                else:
                    for parent in grandparent["children"]:
                        if parent["first_name"] == member["parent"]:
                            if "children" in parent:
                                parent["children"].append(member)
                            else:
                                parent["children"] = [member]
        else:
            self._members.append(member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                saved_index = i
        removed = self._members.pop(saved_index)
        return removed

    def get_member(self, id):
        # fill this method and update the return
        for person in self._members:
            if person["id"] == id:
                return person
        return None 

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

    def get_descendants(self, id):
        children = []
        grandchildren = []
        for grandparent in self._members:
            if grandparent["id"] == id:
                for child in grandparent["children"]:
                    children.append(child["first_name"])
                    if "children" in child:
                        for grandchild in child["children"]:
                            grandchildren.append(grandchild["first_name"])
                return {"children": children, "grandchildren": grandchildren}
            else:
                for parent in grandparent["children"]:
                        if parent["id"] == id:
                            if "children" in parent:
                                for child in parent["children"]:
                                    children.append(child["first_name"])
                            return {"children": children}
                           
                