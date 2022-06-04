# LEARN How to return diffrent DTO type from constructor of factory object
# 
# # from config4 import DevConfig, GlobalConfig, ProdConfig
# from typing import Optional


# class FactoryConfig:
#     """Returns a config instance dependending on the ENV_STATE variable."""

#     def __init__(self, env_state: Optional[str]):
#         self.env_state = env_state

#     def __call__(self):
#         if self.env_state == "dev":
#             return DevConfig()

#         elif self.env_state == "prod":
#             return ProdConfig()

# print(GlobalConfig().ENV_STATE)
# cnf = FactoryConfig(GlobalConfig().ENV_STATE)()
# print(cnf)