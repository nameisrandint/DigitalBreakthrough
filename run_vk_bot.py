import logging
import proj_logger

from configs import ProjConfig
from bots.vk_bot import VkBot


if __name__ == '__main__':
    args = ProjConfig.argument_parser().parse_args()
    log_level: str = args.log_level.upper()
    logging.getLogger().setLevel(log_level)  # setting logging level to the root logger

    orig_config = ProjConfig.init_from_yml(args.yml_path)
    vk = VkBot(orig_config)
    vk.start_vk_bot()
