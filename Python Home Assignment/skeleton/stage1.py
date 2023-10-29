import json

class PolicyAPI:
    def __init__(self) -> None:
        self.policies = []
        self.policy_name_to_obj = {}

    def create_policy(self, json_input: str) -> str:
        try:
            policy_data = json.loads(json_input)

            name = policy_data.get("name")
            if name in self.policy_name_to_obj:
                raise Exception(f"Policy with name '{name}' already exists.")

            if not (isinstance(name, str) and name.isalnum() and len(name) <= 32):
                raise Exception("Invalid policy name.")

            if "description" not in policy_data:
                raise Exception("Missing 'description' field.")

            self.policies.append(policy_data)
            self.policy_name_to_obj[name] = policy_data

            return json.dumps(policy_data)
        except (json.JSONDecodeError, KeyError):
            raise Exception("Invalid JSON input or missing required fields.")

    def list_policies(self) -> str:
        return json.dumps(self.policies)



