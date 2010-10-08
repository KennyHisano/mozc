# Copyright 2010, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'variables': {
    'relative_dir': 'session',
    'gen_out_dir': '<(SHARED_INTERMEDIATE_DIR)/<(relative_dir)',
  },
  'targets': [
    {
      'target_name': 'session',
      'type': 'static_library',
      'sources': [
        'internal/candidate_list.cc',
        'internal/keymap.cc',
        'internal/session_normalizer.cc',
        'internal/session_output.cc',
        'session.cc',
        'session_converter.cc',
        'session_handler.cc',
        'session_observer_handler.cc',
        'session_server.cc',
        'session_usage_observer.cc',
        'session_watch_dog.cc',
      ],
      'dependencies': [
        '../protobuf/protobuf.gyp:protobuf',
        '../base/base.gyp:base',
        '../client/client.gyp:client',
        '../composer/composer.gyp:composer',
        '../converter/converter.gyp:converter',
        '../rewriter/calculator/calculator.gyp:calculator',
        '../usage_stats/usage_stats.gyp:usage_stats',
        'config_handler',
        'genproto_session',
        'ime_switch_util',
        'key_parser',
        'keymap',
        'session_protocol',
      ],
    },
    {
      'target_name': 'config_handler',
      'type': 'static_library',
      'sources': [
        'config_handler.cc',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:config_file_stream',
        'genproto_session',
        'session_protocol',
      ],
    },
    {
      'target_name': 'key_parser',
      'type': 'static_library',
      'sources': [
        'key_parser.cc',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        'genproto_session',
        'session_protocol',
      ],
    },
    {
      'target_name': 'keymap',
      'type': 'static_library',
      'sources': [
        'internal/keymap.cc',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        'genproto_session',
        'session_protocol',
      ],
    },
    {
      'target_name': 'ime_switch_util',
      'type': 'static_library',
      'sources': [
        'ime_switch_util.cc',
        'internal/keymap.cc',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:config_file_stream',
        'config_handler',
        'key_parser',
        'genproto_session',
        'session_protocol',
      ],
    },
    {
      'target_name': 'random_keyevents_generator',
      'type': 'static_library',
      'sources': [
        'random_keyevents_generator.cc',
        '<(gen_out_dir)/session_stress_test_data.h',
      ],
      'dependencies': [
        'session',
        'genproto_session',
        'session_protocol',
        'gen_session_stress_test_data',
      ],
    },
    {
      'target_name': 'genproto_session',
      'type': 'none',
      'sources': [
        'commands.proto',
        'config.proto',
        'state.proto',
      ],
      'includes': [
        '../protobuf/genproto.gypi',
      ],
    },
    {
      'target_name': 'session_protocol',
      'type': 'static_library',
      'sources': [
        '<(proto_out_dir)/<(relative_dir)/commands.pb.cc',
        '<(proto_out_dir)/<(relative_dir)/config.pb.cc',
        '<(proto_out_dir)/<(relative_dir)/state.pb.cc',
      ],
      'dependencies': [
        '../protobuf/protobuf.gyp:protobuf',
        'genproto_session'
      ],
    },
    {
      'target_name': 'session_server_main',
      'type': 'executable',
      'sources': [
        'session_server_main.cc',
      ],
      'dependencies': [
        'session',
        'session_protocol',
      ],
    },
    {
      'target_name': 'session_test',
      'type': 'executable',
      'sources': [
        'session_test.cc',
      ],
      'dependencies': [
        'session',
        '../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'small',
      },
    },
    {
      'target_name': 'session_regression_test',
      'type': 'executable',
      'sources': [
        'session_regression_test.cc',
      ],
      'dependencies': [
        'session',
        '../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'large',
      },
    },
    {
      'target_name': 'session_handler_test',
      'type': 'executable',
      'sources': [
        'session_handler_test.cc',
      ],
      'dependencies': [
        'session',
        '../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'small',
      },
    },
    {
      'target_name': 'session_converter_test',
      'type': 'executable',
      'sources': [
        'session_converter_test.cc',
      ],
      'dependencies': [
        'session',
        '../testing/testing.gyp:gtest_main',
      ],
    },
    {
      'target_name': 'session_module_test',
      'type': 'executable',
      'sources': [
        'config_handler_test.cc',
        'ime_switch_util_test.cc',
        'session_observer_handler_test.cc',
        'session_usage_observer_test.cc',
        'session_watch_dog_test.cc',
      ],
      'dependencies': [
        'session',
        '../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'small',
        'test_data': [
          '../<(test_data_subdir)/session_usage_observer_testcase1.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase2.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase3.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase4.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase5.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase6.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase7.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase8.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase9.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase10.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase11.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase12.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase13.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase14.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase15.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase16.txt',
          '../<(test_data_subdir)/session_usage_observer_testcase17.txt',
        ],
        'test_data_subdir': 'data/test/session',
      },
      'includes': ['../gyp/install_testdata.gypi'],
    },
    {
      'target_name': 'session_internal_test',
      'type': 'executable',
      'sources': [
        'internal/candidate_list_test.cc',
        'internal/keymap_test.cc',
        'internal/session_normalizer_test.cc',
        'internal/session_output_test.cc',
      ],
      'dependencies': [
        'session',
        '../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'small',
      },
    },
    {
      'target_name': 'session_handler_stress_test',
      'type': 'executable',
      'sources': [
        'session_handler_stress_test.cc'
      ],
      'dependencies': [
        'session',
        'random_keyevents_generator',
        '../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'small',
      },
    },
    {
      'target_name': 'random_keyevents_generator_test',
      'type': 'executable',
      'sources': [
        'random_keyevents_generator_test.cc',
      ],
      'dependencies': [
        'random_keyevents_generator',
        '../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'large',
      },
    },
    {
      'target_name': 'gen_session_stress_test_data',
      'type': 'none',
      'actions': [
        {
          'action_name': 'gen_session_stress_test_data',
          'inputs': [
            '../data/test/stress_test/sentences.txt',
          ],
          'outputs': [
            '<(gen_out_dir)/session_stress_test_data.h'
          ],
          'action': [
            'python', '../build_tools/redirect.py',
            '<(gen_out_dir)/session_stress_test_data.h',
            'gen_session_stress_test_data.py',
            '../data/test/stress_test/sentences.txt',
          ],
          'message': 'Generating <(gen_out_dir)/session_stress_test_data.h',
        },
      ],
    },
    {
      'target_name': 'session_converter_stress_test',
      'type': 'executable',
      'sources': [
        'session_converter_stress_test.cc'
      ],
      'dependencies': [
        'session',
        '../testing/testing.gyp:gtest_main',
      ],
      'variables': {
        'test_size': 'large',
      },
    },
    # Test cases meta target: this target is referred from gyp/tests.gyp
    {
      'target_name': 'session_all_test',
      'type': 'none',
      'dependencies': [
        'random_keyevents_generator_test',
        'session_test',
        'session_internal_test',
        'session_internal_test',
        'session_handler_test',
        'session_handler_stress_test',
        'session_module_test',
        'session_converter_test',
        'session_converter_stress_test',
        'session_regression_test',
      ],
    },
  ],
}
