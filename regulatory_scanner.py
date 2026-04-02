# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

import json
import typing


class RegulatoryNewsScanner(gl.Contract):
    has_scanned: bool
    reg_sentiment: str
    key_region: str
    analysis: str
    param: str

    def __init__(self, param: str):
        self.has_scanned = False
        self.reg_sentiment = "NEUTRAL"
        self.key_region = "unknown"
        self.analysis = "Awaiting scan"
        self.param = param

    @gl.public.write
    def scan_regulations(self) -> typing.Any:

        if self.has_scanned:
            return "Already scanned"

        def nondet() -> str:
            fng = gl.nondet.web.render("https://alternative.me/crypto/fear-and-greed-index/", mode="text")
            print(fng)

            task = f"""You are a crypto regulatory analyst. Based on market fear level, assess the regulatory environment.
            Here is current crypto market data:
            {fng[:1500]}

            Respond with the following JSON format:
            {{
                "reg_sentiment": str,
                "key_region": str,
                "policy_type": str,
                "summary": str
            }}
            reg_sentiment: one of VERY_HOSTILE, HOSTILE, NEUTRAL, FRIENDLY, VERY_FRIENDLY.
            key_region: most impactful regulatory region right now.
            policy_type: one of BAN, RESTRICTION, FRAMEWORK, APPROVAL, ADOPTION.
            summary: one sentence about regulatory landscape.
            It is mandatory that you respond only using the JSON format above,
            nothing else. Don't include any other words or characters,
            your output must be only JSON without any formatting prefix or suffix.
            This result should be perfectly parsable by a JSON parser without errors.
            """
            result = gl.nondet.exec_prompt(task).replace("```json", "").replace("```", "")
            print(result)
            return json.dumps(json.loads(result), sort_keys=True)

        result_json = json.loads(gl.eq_principle.strict_eq(nondet))

        self.has_scanned = True
        self.reg_sentiment = result_json["reg_sentiment"]
        self.key_region = result_json["key_region"]
        self.analysis = result_json["summary"]

        return result_json
