# -*- coding: utf-8 -*-

import argparse, logging, sys

from unittest.mock import patch

import pytest

from profiler2 import helpers


class TestHelpers:
    @pytest.mark.parametrize(
        "args,expected",
        [(["--logging", "debug"], 10), (["--logging", "warning"], 30), ([], 20),],
    )
    def test_logger(self, args, expected):
        parser = helpers.setup_parser()
        helpers.setup_logger(parser.parse_args(args))
        assert logging.root.level == expected

    @pytest.mark.parametrize(
        "channel,expected",
        [
            ("0", "not a valid"),
            ("1", 1),
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("10", 10),
            ("11", 11),
            ("12", 12),
            ("13", 13),
            ("36", 36),
            ("40", 40),
            ("44", 44),
            ("48", 48),
            ("52", 52),
            ("56", 56),
            ("60", 60),
            ("64", 64),
            ("100", 100),
            ("104", 104),
            ("108", 108),
            ("112", 112),
            ("116", 116),
            ("120", 120),
            ("124", 124),
            ("128", 128),
            ("132", 132),
            ("136", 136),
            ("140", 140),
            ("149", 149),
            ("153", 153),
            ("157", 157),
            ("161", 161),
            ("165", 165),
        ],
    )
    def test_channel(self, channel, expected):
        if channel == "0":
            with pytest.raises(argparse.ArgumentTypeError) as exc_info:
                channel = helpers.check_channel(channel)
                print(exc_info)
                assert "not a valid channel" in exc_info
        else:
            channel = helpers.check_channel(channel)
            assert channel == expected

    def test_config(self):
        parser = helpers.setup_parser()
        config = helpers.setup_config(
            parser.parse_args(["--config", "tests/config.ini"])
        )
        assert "GENERAL" in config.keys()
        for _ in (
            "channel",
            "ssid",
            "interface",
            "ft_disabled",
            "he_disabled",
            "listen_only",
            "hostname_ssid",
            "files_path",
        ):
            assert _ in config["GENERAL"].keys()

    def test_config_not_present(self):
        parser = helpers.setup_parser()
        with pytest.raises(SystemExit) as pytest_wrapped_exit:
            config = helpers.setup_config(parser.parse_args(["--config", "fake.ini"]))
        assert pytest_wrapped_exit.type == SystemExit
