"""
Docstring for myapp.Pages.home
"""

import time
from datetime import datetime

import pytz
import streamlit as st

from myapp.common.constants import HTTP_OK
from myapp.common.state_manager import CurrentChat
from myapp.common.state_manager import StateManager as sm
from myapp.common.ui_components import my_text, toast_success, toast_warning


def get_time():
    """
    Docstring for get_time
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")


def utc_to_ist(utc_time):
    """
    Docstring for utc_to_ist

    :param utc_time: Description
    """
    utc_format = "%Y-%m-%d %H:%M:%S"
    utc_naive_dt = datetime.strptime(utc_time, utc_format)
    utc_aware_dt = pytz.utc.localize(utc_naive_dt)
    ist_timezone = pytz.timezone("Asia/Kolkata")
    ist_time = str(utc_aware_dt.astimezone(ist_timezone))
    return ist_time[: len(ist_time) - 6]


class Home:
    """
    Docstring for Home
    """

    def logout(self):
        """
        Docstring for logout

        :param self: Description
        """
        sm.set_authenticated(False)
        st.rerun()

    @st.dialog("Add Users")
    def add_user_dialog(self):
        """
        Docstring for addUserDialog

        :param self: Description
        """
        users = sm.get_container().chat_service.get_not_in_chat(self.user.userID)
        users_dict = {item[0]: item[1] for item in users.content}

        selected_users = st.multiselect("Users", options=users_dict.keys())
        with st.container(horizontal=True):
            if st.button("Cancel"):
                st.rerun()
            if st.button("Add", type="primary"):
                for i in selected_users:
                    # st.write(self.user.userID, users_dict[i])
                    sm.get_container().chat_service.add(self.user.userID, users_dict[i])
                toast_success(f"Successfully Added users {selected_users}")
                st.rerun()

    @st.dialog("Do you really want to block?")
    def confirm_block(self, chat_id):
        """
        Docstring for confirm_block

        :param self: Description
        :param chat_id: Description
        """
        with st.container(horizontal=True):
            if st.button("No"):
                st.rerun()
            if st.button("Yes", type="primary"):
                sm.get_container().chat_service.update_block(
                    self.user.userID, chat_id, is_blocked=True
                )
                toast_success("Blocked!")
                time.sleep(1)
                st.rerun()

    @st.dialog("Do you want to unblock?")
    def confirm_unblock(self, chat_id):
        """
        Docstring for confirm_unblock

        :param self: Description
        :param chat_id: Description
        """
        with st.container(horizontal=True):
            if st.button("No"):
                st.rerun()
            if st.button("Yes", type="primary"):
                sm.get_container().chat_service.update_block(
                    self.user.userID, chat_id, is_blocked=False
                )
                # Friends_Services().unblock_user(friend_uid)
                toast_success("Un-Blocked!")
                time.sleep(1)
                st.rerun()

    @st.dialog("Do you really want to delete account?")
    def confirm_delete_account(self):
        """
        Docstring
        """
        with st.container(horizontal=True):
            if st.button("No"):
                st.rerun()
            if st.button("Yes", type="primary"):
                sm.get_container().user_service.delete_account(
                    self.user.userID,
                )
                # Friends_Services().unblock_user(friend_uid)
                toast_success("Successfully Deleted account!")
                time.sleep(1)
                self.logout()

    @st.dialog("Enter Broadcast Message")
    def broadcast(self):
        """
        Docstring for broadcast

        :param self: Description
        """
        msg = st.text_input("", placeholder="Your message")
        if st.button("Send", type="primary"):
            if msg.strip() == "":
                toast_warning("Enter Msg")
                return
            # Chat_Services.broadcast(msg)
            toast_success(
                "Msg Broadcasted Successfully!",
            )
            time.sleep(1)
            st.rerun()

    @st.dialog("Create Group")
    def create_group_dialog(self):
        """
        Docstring for createGroupDialog

        :param self: Description
        """
        grp_name = st.text_input("Group Name").strip()
        res = sm.get_container().chat_service.get_all(self.user.userID)
        users = [] if res.status != HTTP_OK else res.content
        # if res.status != HTTP_OK:
        #     users = []
        # else:
        #     users = res.content
        users_dict = {user.userName: user.userID for user in users}
        grp_members = st.multiselect("Members", users_dict.keys())
        with st.container(horizontal=True):
            if st.button("Cancel"):
                st.rerun()
            if st.button("Create", type="primary"):
                if grp_name == "":
                    toast_warning("Fill the Group Name!")
                    return
                members_id = [users_dict[grpMember] for grpMember in grp_members]
                sm.get_container().group_service.create_group(
                    self.user.userID, grp_name, members_id
                )
                toast_success("Group Created Successfully!")
                time.sleep(2)
                st.rerun()
                # st.write(grp_name)
                # st.write(grp_members)

    def contact_tile(self, chat_id: int, user_name: str):
        """
        Docstring for contact_tile

        :param self: Description
        :param chat_id: Description
        :type chat_id: int
        :param user_name: Description
        :type user_name: str
        """
        with st.container(horizontal=True, border=False):
            if st.button(
                user_name.capitalize(),
                width="stretch",
                key=f"{chat_id}1",
                use_container_width=True,
                icon=":material/person:",
            ):
                sm.set_current_chat(CurrentChat(chat_id, user_name, "DM"))

            with st.popover("", type="tertiary", width=10):
                if st.button("Remove", key=f"{chat_id}2", width="stretch"):
                    # Friends_Services.remove_friend(User_Services.get_user().uid, user[0])
                    toast_success("User removed successfully!")
                    time.sleep(1)
                    st.rerun()
                if st.button("Block", key=f"{chat_id}3", width="stretch"):
                    self.confirm_block(
                        chat_id,
                    )

    def sidebar(self):
        """
        Docstring for sidebar

        :param self: Description
        """
        with st.sidebar.container(horizontal_alignment="center"):
            my_text("~ Talksy ~", size="h3", alignment="center")
            my_text(
                f"Welcome {self.user.userName.capitalize()}",
                size="h1",
                alignment="center",
                padding=False,
            )
        st.sidebar.divider()
        contacts, groups, blocked, options = st.sidebar.tabs(
            ["Contacts", "Groups", "Blocked", "Options"]
        )
        with contacts:
            res = sm.get_container().chat_service.get_all(self.user.userID)
            if res.status == HTTP_OK:
                users = res.content
                for user in users:
                    if user.blocked != 1:
                        self.contact_tile(user.chatID, user.userName)
                    else:
                        with blocked:
                            if st.button(
                                user.userName, width="stretch", icon=":material/block:"
                            ):
                                # pass
                                self.confirm_unblock(user.chatID)
            # if st.button('Broadcast', width='stretch'):
            #     self.broadcast()

        with options:
            st.button(
                "Add User to Chat",
                width="stretch",
                type="primary",
                icon=":material/person_add:",
                on_click=self.add_user_dialog,
            )

            st.button(
                "Create Group",
                width="stretch",
                type="primary",
                icon=":material/groups_3:",
                on_click=self.create_group_dialog,
            )

            st.button(
                "Logout",
                width="stretch",
                type="primary",
                icon=":material/logout:",
                on_click=self.logout,
            )

            st.button(
                "Delete Account",
                width="stretch",
                type="primary",
                icon=":material/delete:",
                on_click=self.confirm_delete_account,
            )

        with groups:
            res = sm.get_container().group_service.get_all_groups(self.user.userID)
            if res.status != HTTP_OK:
                return
            grps = res.content
            for grp in grps:
                with st.container(horizontal=True):
                    if st.button(
                        grp.name,
                        key=f"{grp.id}-1",
                        width="stretch",
                        type="primary",
                        icon=":material/group:",
                    ):
                        sm.set_current_chat(CurrentChat(grp.id, grp.name, "GROUP"))
                    with st.popover("", type="tertiary", width=10):
                        if st.button(
                            "Add Members",
                            key=f"{grp.id}-2",
                            icon=":material/person_add:",
                        ):
                            if grp.role == "ADMIN":
                                pass
                            elif grp.role == "MEMBER":
                                toast_warning("Only admin can add members")

    def chat_tile(self, user_name, user_id, msg, chat_time, msg_id, *, seen=True):
        """
        Docstring for chat_tile

        :param self: Description
        :param user_name: Description
        :param user_id: Description
        :param msg: Description
        :param chat_time: Description
        :param msg_id: Description
        :param seen: Description
        """
        with (
            st.chat_message(
                "human",
                avatar=":material/account_box:"
                if user_id == self.user.userID
                else None,
            ),
            st.container(horizontal=True, vertical_alignment="center"),
        ):
            st.text(f"{user_name} :")
            st.markdown(msg)
            with st.container(
                horizontal=True,
                horizontal_alignment="right",
                vertical_alignment="center",
            ):
                my_text(chat_time, size="p", alignment="right", padding=False)
                if user_id == self.user.userID:
                    st.badge(
                        "",
                        icon=":material/check:" if not seen else ":material/done_all:",
                    )
                    with st.popover("", type="tertiary"):
                        if st.button("Delete Msg", key=f"{user_id}-{chat_time}"):
                            sm.get_container().msg_service.delete_msg(msg_id)
                            st.rerun()

                else:
                    st.space(size=56)
                    # if st.button("Delete Msg", key= msg_id, icon=':material/delete:'):
                    #     # st.write(msg_id)
                    #     pass
                    #     # Chat_Services.del_chat(msg_id)
                    #     # st.rerun()

    def chat(self):
        """
        Docstring for chat

        :param self: Description
        """
        current_chat = sm.get_current_chat()
        if current_chat is None:
            my_text("~ Talksy ~", size="h1", padding=False)
            st.divider()
            with st.container(
                border=False,
                height=500,
                horizontal_alignment="center",
                vertical_alignment="center",
            ):
                my_text("Welcome to Talksy", size="h2", alignment="center")
                my_text("Select a contact to chat...!", size="h5", alignment="center")
            return

        chat_container = st.container(border=True, width="stretch", height=680)

        with chat_container:
            with st.container(horizontal=True):
                st.title(current_chat.chatName.capitalize())
                if st.button("close", icon=":material/tab_close:", type="primary"):
                    sm.set_current_chat(None)
                    st.rerun()
            st.divider()
            res = sm.get_container().msg_service.get_all_message(
                self.user.userID, current_chat.chatID, current_chat.type
            )
            # st.write(msgs)
            if res.status == HTTP_OK:
                msgs = res.content
                for msg in msgs:
                    # st.write(msg)
                    self.chat_tile(
                        msg.userName,
                        msg.userID,
                        msg.msg,
                        utc_to_ist(msg.sentAt),
                        msg.chat_id,
                        # seen=False if msg.seenAt is None else True,
                        seen=not msg.seenAt,
                    )

        if new_msg := st.chat_input():
            with chat_container:
                # pass
                self.chat_tile(
                    self.user.userName,
                    self.user.userID,
                    new_msg,
                    get_time(),
                    11,
                    seen=False,
                )
                current_chat = sm.get_current_chat()
                if current_chat is not None:
                    sm.get_container().msg_service.add_message(
                        new_msg,
                        self.user.userID,
                        current_chat.chatID,
                        current_chat.type,
                    )

    def __init__(self):
        user = sm.get_user()
        if user is not None:
            self.user = user
        print()
        self.sidebar()
        self.chat()
        # if "read_chat_uid" in st.session_state:
        #     Chat_Services.update_msg_read_status()
        #     # toast_success('msg_seen')
        #     del st.session_state["read_chat_uid"]


def main():
    """
    Docstring for main
    """
    Home()


if __name__ == "__main__":
    main()
