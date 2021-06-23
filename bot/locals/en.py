
from bot.locals import Local

LOCAL = Local({
    'WRONG_ROOM' : 'I a\'m not suppose to be here.\nID : <code>{-1001400005258}</code>',
    'WELCOME_MESSAGE' : "Hi!\nI'm <b>Botkaca</b>!\nPowered by pyrogram.\nFork: <a href='https://github.com/Finitebottutu/botkaca'>github.com/Finitebottutu/botkaca</a>",
    'PASS_REQUIRED' : '\n\nUse <code>/{cmd_pass} </code>to enter the password.',
    'LEECH_LIST_MESSAGE_HEADER' : '<b>Leech Status</b>',
    'LEECH_LIST_FORMAT' : 'Name: <code>{name}</code>\nStatus: {status}\nID: <code>{gid}</code>\n\n',
    'ARIA2_CHECKING_LINK' : "Checking...",
    'ARIA2_DOWNLOAD_STATUS' : "Downloading : <code>{name}</code>\n{block} {percentage}\nSize : {total_size}\nDN : {download_speed} / UP : {upload_speed}\nSeeder : {seeder}\nETA : {eta}\nID : <code>{gid}</code>",
    'ARIA2_DOWNLOAD_SUCCESS' : 'File downloaded : <code>{name}</code>',
    'ARIA2_DOWNLOAD_CANCELED' : 'Download canceled : <code>{name}</code>',
    'ARIA2_DEAD_LINK' : 'Download auto canceled : <code>{name}</code>\nYour Torrent/Link is Dead.',
    'ARIA2_NO_URI' : 'Link is invalid.',
    'UPLOADING_FILE' : 'Uploading : <code>{name}</code>',
    'UPLOADING_PROGRESS' : 'Uploading : <code>{name}</code>\n{block} {percentage}%\nSize : {size}\nUP : {upload_speed}/s\nETA : {eta}',
    'UPLOAD_FAILED_FILE_MISSING' : 'Upload : Failed. file not found.\n<code>{name}</code>',
    'GENERATE_THUMBNAIL' : 'Thumbnail : Generating.\n<code>{name}</code>',
    'SPLIT_FILE' : 'Spliting : <code>{name}</code>',
    'SPLIT_FAILED' : 'Split : Failed.\n<code>{name}</code>',
    'THUMBNAIL_NO_PHOTO' : 'Set <code>/{cmd_set_thumbnail}</code> as your photo caption.',
    'THUMBNAIL_DOWNLOADING' : 'Downloading thumbnail.',
    'THUMBNAIL_DOWNLOADED' : 'Thumbnail download.',
    'THUMBNAIL_APPLIED' : 'Thumbnail applied.',
    'THUMBNAIL_DELETING' : 'Deleting thumbnail.',
    'THUMBNAIL_RESET' : 'Thumbnail reset.',
    'UPLOAD_AS_DOC' : 'Upload as document set to {status}.',
    'UPLOAD_AS_ZIP' : 'Upload as zip file set to {status}.',
    'TRACKER_RESET' : 'Default torrent tracker reset.',
    'TRACKER_APPLIED' : 'Default torrent tracker applied.',
    'HELP_MESSAGE_HEADER' : '<b>Bot Command</b>',
    'NO_HELP_INFO' : 'no information',
    'COMMAND_START' : 'start bot',
    'COMMAND_PASSWORD' : 'enter password that required',
    'COMMAND_HELP' : 'this message',
    'COMMAND_LEECH' : 'leech link or magnet',
    'COMMAND_CANCEL_LEECH' : 'cancel leeching',
    'COMMAND_LEECH_LIST' : 'list on going leech',
    'COMMAND_SET_THUMBNAIL' : 'set custom video thumbail',
    'COMMAND_RESET_THUMBNAIL' : 'reset custom video thumbnail',
    'COMMAND_UPLOAD_AS_DOC' : 'toggle upload anything as document',
    'COMMAND_UPLOAD_AS_ZIP' : 'toggle upload anything as bundled zipfile',
    'COMMAND_SET_TRACKER' : 'set default tracker, sparated by newline',
    'BLOCK_EMPTY' : "▱",
    "BLOCK_FILLED" : "▰"
})
